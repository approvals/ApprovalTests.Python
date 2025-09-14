#!/usr/bin/env python3
"""
Delinter - Automated linting fix process

This script implements the delinter process:
1. Run tests to ensure they pass
2. Run linting and capture results
3. Use Claude to fix the first linting issue
4. Run tests again to ensure they still pass
5. If tests pass, commit changes; otherwise revert
6. Repeat up to 10 times
"""

import subprocess
import sys
import os
import tempfile
from pathlib import Path
from typing import Tuple


def run_command(cmd: str, capture_output: bool = True, check: bool = True) -> Tuple[int, str, str]:
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=capture_output, 
            text=True, 
            check=check
        )
        if capture_output:
            return result.returncode, result.stdout, result.stderr
        else:
            return result.returncode, "", ""
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout if capture_output else "", e.stderr if capture_output else ""


def run_tests() -> bool:
    """Run tests using mise test."""
    print("Running tests...")
    returncode, stdout, stderr = run_command("check_that_fix_works")
    if returncode == 0:
        print("✅ Tests passed")
        return True
    else:
        print("❌ Tests failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False


def run_linting() -> bool:
    """Run linting and save results to .ignore/lint-results.txt."""
    print("Running linting...")
    
    # Ensure .ignore directory exists
    os.makedirs(".ignore", exist_ok=True)
    
    returncode, stdout, stderr = run_command("find_problems", check=False)
    
    # Check if lint-results.txt was created and has content
    if os.path.exists(".ignore/lint-results.txt"):
        with open(".ignore/lint-results.txt", "r") as f:
            content = f.read().strip()
            if content:
                print(f"Linting found issues, saved to .ignore/lint-results.txt")
                return True
            else:
                print("✅ No linting issues found")
                return False
    else:
        print("❌ Failed to create .ignore/lint-results.txt")
        return False


def fix_with_claude() -> bool:
    """Use Claude to fix the first linting issue."""
    print("Fixing linting issues with Claude...")
    
    # Check if lint.process.md exists
    if not os.path.exists(".mise/lint.process.md"):
        print("❌ .mise/lint.process.md not found")
        return False
    
    # Read the prompt from lint.process.md
    try:
        with open(".mise/lint.process.md", "r") as f:
            prompt_content = f.read().strip()
    except Exception as e:
        print(f"❌ Failed to read .mise/lint.process.md: {e}")
        return False
    
    # Use Claude CLI to fix the issue by passing the prompt as input
    try:
        print("Calling Claude CLI...")
        result = subprocess.run(
            ["claude", "--print", "--dangerously-skip-permissions"],
            input=prompt_content,
            text=True,
            capture_output=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            print("✅ Claude completed fixing")
            return True
        else:
            print("❌ Claude failed to fix issues")
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Claude timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"❌ Error running Claude: {e}")
        return False


def commit_changes() -> bool:
    """Commit changes using the generated commit message."""
    print("Committing changes...")
    
    # Check if commit-message.txt exists
    if not os.path.exists(".ignore/commit-message.txt"):
        print("❌ .ignore/commit-message.txt not found")
        return False
    
    # Stage all changes
    returncode, _, _ = run_command("git add .")
    if returncode != 0:
        print("❌ Failed to stage changes")
        return False
    
    # Commit with the message file
    returncode, stdout, stderr = run_command("git commit -F .ignore/commit-message.txt")
    if returncode == 0:
        print("✅ Changes committed successfully")
        return True
    else:
        print("❌ Failed to commit changes")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False


def revert_changes() -> None:
    """Revert any uncommitted changes."""
    print("Reverting changes...")
    run_command("git checkout .", check=False)
    run_command("git clean -fd", check=False)
    print("✅ Changes reverted")


def play_chime() -> None:
    """Play a small chime sound to indicate completion."""
    try:
        # Use afplay on macOS to play a system sound
        subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"], 
                      check=False, capture_output=True)
    except Exception:
        # Fallback: print a bell character
        print("\a")  # ASCII bell character


def main() -> None:
    """Main delinter process."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Delinter - Automated linting fix process",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run full delinter process
  %(prog)s --dry-run          # Show what would be done without making changes
  %(prog)s --max-iter 5       # Limit to 5 iterations
  %(prog)s --test-only        # Only run tests, don't fix linting
  %(prog)s --lint-only        # Only run linting, don't fix issues
        """
    )
    
    parser.add_argument(
        "--dry-run", 
        action="store_true",
        help="Show what would be done without making any changes"
    )
    
    parser.add_argument(
        "--max-iter", 
        type=int, 
        default=1000,
        help="Maximum number of iterations (default: 10)"
    )
    
    parser.add_argument(
        "--test-only", 
        action="store_true",
        help="Only run tests, don't fix linting issues"
    )
    
    parser.add_argument(
        "--lint-only", 
        action="store_true",
        help="Only run linting, don't fix issues"
    )
    
    parser.add_argument(
        "--skip-initial-tests", 
        action="store_true",
        help="Skip initial test run (use with caution)"
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting delinter process...")
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    
    # Change to the repository root
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)
    print(f"Working directory: {os.getcwd()}")
    
    # Test-only mode
    if args.test_only:
        print("\n🧪 Running tests only...")
        if run_tests():
            print("✅ Tests passed!")
            return
        else:
            print("❌ Tests failed!")
            sys.exit(1)
    
    # Lint-only mode
    if args.lint_only:
        print("\n🔍 Running linting only...")
        if run_linting():
            print("⚠️ Linting issues found - check .ignore/lint-results.txt")
            return
        else:
            print("✅ No linting issues found!")
            return
    
    # Full delinter process
    max_iterations = args.max_iter
    
    for iteration in range(1, max_iterations + 1):
        print(f"\n--- Iteration {iteration}/{max_iterations} ---")
        
        # Step 1: Run tests to ensure they pass initially (unless skipped)
        if not args.skip_initial_tests or iteration == 1:
            if args.dry_run:
                print("🔍 Would run: mise test")
            else:
                if not run_tests():
                    print("❌ Initial tests failed. Aborting.")
                    sys.exit(1)
        
        # Step 2: Run linting
        if args.dry_run:
            print("🔍 Would run: mise lint1 | tee .ignore/lint-results.txt")
            print("🔍 Would check for linting issues")
            # In dry-run mode, simulate finding issues for demonstration
            if iteration > 3:  # Simulate completing after a few iterations
                print("🔍 Would find no more linting issues")
                break
        else:
            if not run_linting():
                print("✅ No more linting issues found. Delinter complete!")
                break
        
        # Step 3: Use Claude to fix linting issues
        if args.dry_run:
            print("🔍 Would call Claude CLI to fix issues")
        else:
            if not fix_with_claude():
                print("❌ Claude failed to fix issues. Aborting.")
                sys.exit(1)
        
        # Step 4: Run tests again to ensure they still pass
        if args.dry_run:
            print("🔍 Would run tests again")
            print("🔍 Would commit changes if tests pass, or revert if they fail")
        else:
            if run_tests():
                # Tests pass, commit the changes
                if commit_changes():
                    print(f"✅ Iteration {iteration} completed successfully")
                    play_chime()  # Play chime after successful iteration
                    # Clean up temporary files
                    for temp_file in [".ignore/lint-results.txt", ".ignore/commit-message.txt"]:
                        if os.path.exists(temp_file):
                            os.remove(temp_file)
                else:
                    print("❌ Failed to commit, reverting changes")
                    revert_changes()
            else:
                # Tests failed, revert changes
                print("❌ Tests failed after fixes, reverting changes")
                revert_changes()
    
    else:
        print(f"❌ Reached maximum iterations ({max_iterations}). Some issues may remain.")
        if not args.dry_run:
            sys.exit(1)
    
    if args.dry_run:
        print("\n🔍 Dry run completed - no changes were made")
    else:
        print("\n🎉 Delinter process completed successfully!")


if __name__ == "__main__":
    main()
