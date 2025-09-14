# AI Loop Fixer

This is a python script 
Detects an issue and tries to fix it in a loop.

```mermaid
flowchart TD
    Start([START<br/>PYTHON]) --> RunTests1{check_that_fix_works}
    RunTests1 -->|FAIL| Exit([EXIT/ABORT<br/>PYTHON])
    RunTests1 -->|PASS| RunLint["find_problems"]
    
    RunLint --> HasIssues{has_problems}
    HasIssues -->|NO| Done([ALL DONE<br/>PYTHON])
    HasIssues -->|YES| CallClaude[fix_problem] --> check_that_fix_works
    
  
  

    
    check_that_fix_works -->|NO| Revert[Revert Changes<br/>PYTHON]
    check_that_fix_works -->|YES| Commit["commit"]
    
    Commit --> Chime["Play Chime<br/>PYTHON"]
    Chime --> RunLint

    Revert --> RunLint
    

    

    
    %% End states
    style Done fill:#2e7d32,stroke:#1b5e20,stroke-width:2px,color:#fff
    style Exit fill:#c62828,stroke:#b71c1c,stroke-width:2px,color:#fff
```

## Scripts

The scripts are along side the python script, but all run from the repos base directory.

* check_that_fix_works
* find_problems
* fix_problems
* commit

on windows the scripts are .cmd files, on linux they are .sh files without an extension. This means you can run them from the command line like this:

```
./find_problems
```

## Git revert
`git reset --hard`

### Chime

After each successful iteration (commit), the script plays a system chime sound (Glass.aiff on macOS) (?? on windows) to notify that the iteration is complete.
