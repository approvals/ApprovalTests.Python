# Approval Testing Concepts


toc

For Intention Only:
Diagram representing the workflow of a dev using approval tests
The user will have tasks
User tasks / actions
User sees

## Developer Workflow
digraph G { node [style=filled, shape=rect]

* Separate steps with user vs automatic

User would do:
- approvaltests already installed
- user does: write new test -> run the test

## Running Approvals
```mermaid
flowchart
Run --> capture(Captures Snapshot) --> comp(Compares Snapshot) --> Passes 
comp --> Fails
Fails --> reporter["Open Reporter (Diff Tool)"]
```

## Add Behavior to Existing Approval
If you are fixing a bug (or adding a feature), this will change the expected behavior. Therefore when you run the test, it will fail.

```mermaid
flowchart
mod(Modify Code) --> run(Run Test)
--> fail["Fail (Expected)"]  
--> diff(Diff Tool)  
--> compare(Review Changes)
-->wanted[Wanted Change]
style wanted fill:#0f0
compare --> unwanted(Unwanted Change)
style unwanted fill:#f00
unwanted --> mod
wanted --> approve(Approve New File)
```

## New Approval
Because the `.approved` file does not exist when writing a new test, the test will always fail the first time you run it.

```mermaid
flowchart
write(Write Test) 
--> code(Write Code) 
--> runt(Run Test) 
--> fail["Fail(Forced)"]
--> diff(Diff Tool)
--> review(Review Result)
--> complete(Feature Complete)
review --> incomplete(Feature Incomplete)
complete --> approve(Approve New File)
incomplete --> code
style incomplete fill:#f00
style complete fill:#0f0
```


## TDD and ApprovalTests

### TDD using Asserts
Test Driven Development usually follows this path:
```mermaid
flowchart
write("Write Test\n(with Expected Result)") --> 
red(See it Fail) --> 
code(Write Code) --> 
green(See it Pass) --> 
refactor(Refactor) --> write
code --> red
style red fill:#f00
style green fill:#0f0
```

### TDD using ApprovalTests
The ApprovalTests loop is slightly different than traditional TDD.
It splits the writing of the test into 2 parts:
1. Writing the Test 
1. Capturing the Expected Result

And moves the capturing of the expected result to after the code is written.

```mermaid
flowchart
write("Write Test\n(without Expected Result)") -->
code(Write Code) -->
assess(Assess the Result) -->
approve(Approve it:\n Capture Expected Result) --> refactor(Refactor) --> write
assess --> code
style approve fill:#0f0
```

### TDD 

<extra notes here>

## Tactics

### Approving Files

Copying from the recieved into the appproved. This can be done on the file system or directly in the diff tool.

"Expected Failure"  -> {"failure2", "Pass (unexpected)"} 
GOAL:  capture the Expected result
use Approval Tests to KEEP TRACK of passing tests



