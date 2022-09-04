# Getting Started with a Mimimal Example

<!-- toc -->
## Contents

  * [Steps](#steps)
    * [1. Install Dependencies](#1-install-dependencies)
    * [2. Create the test file](#2-create-the-test-file)
    * [3. Run the test](#3-run-the-test)
      * [Section 1: Run Information](#section-1-run-information)
      * [Section 2: ApprovalTests diff report](#section-2-approvaltests-diff-report)
      * [Section 3: How to approve the new result](#section-3-how-to-approve-the-new-result)
      * [Section 4: Summary](#section-4-summary)
    * [4. Approve the results](#4-approve-the-results)
      * [Unix](#unix)
      * [Windows](#windows)
    * [5. Rerun the tests](#5-rerun-the-tests)<!-- endToc -->

## Steps

### 1. Install Dependencies

Open a terminal and run:

```bash
pip install pytest approvaltests pytest-approvaltests
```

### 2. Create the test file

Add a new file called `test_with_approvals.py`

containing:

```py
from approvaltests import verify


def test_with_approvals():
    verify("Hello World")
```

### 3. Run the test

Run the test in the terminal:

```bash
python -m pytest . --approvaltests-use-reporter='PythonNativeReporter' 
```

You should simular output to the following (paths, times, and versions might differ) :
```bash
========================================================================================================= test session starts ========================================================================================================= 
platform win32 -- Python 3.6.7, pytest-7.0.1, pluggy-1.0.0 
rootdir: C:\Code\approvaltests.minimal.example             
plugins: approvaltests-0.2.4                               
collected 1 item                                                                                                                                                                                                                        

--- test_with_approvals.test_with_approvals.approved.txt
+++ test_with_approvals.test_with_approvals.received.txt
@@ -0,0 +1 @@
+Hello World


to approve this result:

move "C:\Code\approvaltests.minimal.example\test_with_approvals.test_with_approvals.received.txt" "C:\Code\approvaltests.minimal.example\test_with_approvals.test_with_approvals.approved.txt"

======================================================================================================= short test summary info ======================================================================================================= 
FAILED test_with_approvals.py::test_with_approvals - approvaltests.approval_exception.ApprovalException: Approval Mismatch, received != approved
========================================================================================================== 1 failed in 0.53s ========================================================================================================== 
```

Let's explore what this output means
#### Section 1: Run Information
```bash
========================================================================================================= test session starts ========================================================================================================= 
platform win32 -- Python 3.6.7, pytest-7.0.1, pluggy-1.0.0 
rootdir: C:\Code\approvaltests.minimal.example             
plugins: approvaltests-0.2.4                               
collected 1 item                                                                                                                                                                                                                        
```

This section states what is being run. Which tools and with directories, it also states that pytest found  `1 item` meaning 1 test th

#### Section 2: ApprovalTests diff report
```bash
--- test_with_approvals.test_with_approvals.approved.txt
+++ test_with_approvals.test_with_approvals.received.txt
@@ -0,0 +1 @@
+Hello World
```

This is the result of the `verify("Hello World")` call. It has failed, and there is reporting the difference between this run and what it was expecting (The `approved` version).
The `approved` version is saved in the `test_with_approvals.test_with_approvals.approved.txt` file. 
Which is current empty, because this is the first time the test has ever been run and the results has **never** been approved.

 
The current results of what was passed to the `verify` method have been saved to the `recieved` file: `test_with_approvals.test_with_approvals.received.txt`

The difference (diff) is being displayed with the pluses and minuses. 
All the changes have a `+` next to them showing that all the changes are added lines.


#### Section 3: How to approve the new result

```bash
to approve this result:

move "C:\Code\approvaltests.minimal.example\test_with_approvals.test_with_approvals.received.txt" "C:\Code\approvaltests.minimal.example\test_with_approvals.test_with_approvals.approved.txt"
```

Once you are seeing the results you want, to `approve` them they must be copied into the `.approved.` file. One way to do this is via the command line. 
The exact command needed for your os will appear here. 
Copy, paste, and running it will `approve` the result. Doing this should make the test pass the next time it is run.

#### Section 4: Summary
```bash
======================================================================================================= short test summary info ======================================================================================================= 
FAILED test_with_approvals.py::test_with_approvals - approvaltests.approval_exception.ApprovalException: Approval Mismatch, received != approved
========================================================================================================== 1 failed in 0.53s ========================================================================================================== 
```

The above summarizes the results of all (1) of the tests run in the session. 

### 4. Approve the results

Copy the `.recieved` to the `.approved.`

#### Unix

```bash
mv -f "test_with_approvals.test_with_approvals.received.txt" "test_with_approvals.test_with_approvals.approved.txt"
```
#### Windows

```bash
move "test_with_approvals.test_with_approvals.received.txt" "test_with_approvals.test_with_approvals.approved.txt"
```

### 5. Rerun the tests

Run the test in the terminal:

```bash
python -m pytest . --approvaltests-use-reporter='PythonNativeReporter' 
```

You should simular output to the following (paths, times, and versions might differ) :
```bash
========================================================================================================= test session starts ========================================================================================================= 
platform win32 -- Python 3.6.7, pytest-7.0.1, pluggy-1.0.0
rootdir: C:\Code\approvaltests.minimal.example
plugins: approvaltests-0.2.4
collected 1 item                                                                                                                                                                                                                        

test_with_approvals.py .                                                                                                                                                                                                         [100%] 

========================================================================================================== 1 passed in 0.05s ========================================================================================================== 
```
