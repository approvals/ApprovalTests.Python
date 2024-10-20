- what language should we write this in?
    - python
    - bash
    - other?
- how do we TDD this?
- standalone script vs. internal to the ApprovalTests library
- absolute path vs. relative path in the log
- how do we ensure it works on all platforms, e.g. `/` vs. `\`?
- where do we put it so it's accessible for all ApprovalTests variants?

NOTES:
what algorithm are we trying to implement?
run all the tests, then check the log file for any files that are stale
if a file is stale,  notify the user
notify the user by showing them a list of all stale approval test files

build and test script would run all the tests
how get the user to  do a full test run?

could be:
step 1: run build and test script
step 2: run stale file check script
step 3: run build and test script again

make a new repo just for this tool
that repo has a file that is "i am an approval test*
give me a list of files

given a log file and a list of files, how do we determine which files are stale?


Identify the next small step towards our goal.
- normalize paths (OS)

do we give the user a notification about stale files?

approved_files_from_fs = find . -name "*.approved.*"
deep_diff(approved_files_from_fs, log)

make sure you identify ALL the items in one list that are not in the other list

fs_bag - log_bag = stale_files

create a sandbox that has a log file and some approved files
the algorithm should find the stale files in the sandbox

create a diff function that takes two lists and returns the differences

Tasks:
- [ ] create a diff function that takes two lists and returns the differences
- [ ] create a function that normalizes paths (relateive to project-root)
- [ ] create one list from logfile contents
- [ ] create one list from file system