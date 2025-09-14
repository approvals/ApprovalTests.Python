# Delinter

This is a python script that reads the .temp/lint-results.txt file and fixes the first issue. All temporary files are stored in the `.temp` directory which is ignored by git.

## Steps

1. Run Tests, Ensure they pass
2. Linting (saves results to `.temp/lint-results.txt`)
3. Claude Fixes Linting (writes commit message to `.temp/commit-message.txt`)
4. Run Tests, Ensure they pass. If they do, commit the changes and play a chime. Otherwise, revert. Repeat up to 1000x by default.

### Running Tests

```
mise test
```

### Linting

```
mise lint1 | tee .temp/lint-results.txt
```

### Fixing

Call claude code on the cli and pass it the prompt lint.process.md file. Have it exit afterwars and use dangerously-skip-permissions to skip the permissions check.

### Committing

```
git add .
git commit -F .temp/commit-message.txt
```

### Chime

After each successful iteration (commit), the script plays a system chime sound (Glass.aiff on macOS) to notify that the iteration is complete.
delinter.md
Displaying delinter.md.