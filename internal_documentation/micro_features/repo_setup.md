# Repo Setup

## Concept

These are the basic dev scripts that every repo should have. They provide a standardized interface for common development tasks that works across different platforms and environments.

The underlying tool is Mise-en-Place, aka "Mise" (https://mise.jdx.dev/), which manages tools and tasks within the project scope without requiring system-wide installations.

The idea is that you can clone a repo on a clean machine, then run one of these scripts, and it will just work (assuming Mise is already installed).

## Prerequisites

1. **Mise** - The only system requirement. All other tools are managed by Mise per-project.

Mise automatically:
- Installs required tools (defined in `.mise.toml`)
- Creates and manages virtual environments  
- Handles dependencies
- Runs tasks with proper environment setup

## Implemented Scripts

### Core Scripts

1. **`build_and_test.sh/.cmd`** - Runs the full build pipeline including tests, type checking, linting, and integration tests
2. **`format_code.sh`** - Formats code using configured formatters
3. **`run_mdsnippets.sh/.cmd`** - Updates markdown documentation with code snippets

### Script Implementation Details

**Bash Scripts (.sh):**
- Include error handling (`set -euo pipefail`)
- Check for Mise availability with helpful error messages
- Use `mise task run` to execute configured tasks
- Support parallel task execution where appropriate

**Windows Scripts (.cmd):**
- Use Git Bash to execute the corresponding `.sh` file
- Provide cross-platform compatibility without duplicating logic

### Configuration

Tasks are defined in `.mise.toml`.
