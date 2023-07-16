# What are Approvals

## General

"Approval Tests" is a software testing tool which allows us to see the effects of our changes while working on our code. The process is streamlined by comparing the output of the code to an expected result.

Approvals is a different way to do assertions in tests.

Instead of

`assert(a==b)`

do

`verify(a)`


## Here's how it works

-   If the changed results match the approved file perfectly, the test passes.
-   If there's a difference, a reporter tool will highlight the mismatch and the test fails. This creates a visual, textual representation of what has been changed.

## How To

In order to use Approval Tests, the user needs to:

1. Set up a test: This involves importing the Approval Tests library into your own code.

2. Optionally, set up a reporter: Reporters are tools that highlight differences between approved and received files when a test fails. Although not necessary, they make it significantly easier to see what changes have caused a test to fail.

3. Manage the "approved" file: When the test is run for the first time, an approved file is created automatically. This file will represent the expected outcome. Once the test results in a favorable outcome, the approved file should be updated to reflect these changes. This is typically done by copying the received file to the approved file.

This setup is useful because it shortens feedback loops, saving developers time by only highlighting what has been altered rather than requiring them to parse through their entire output to see what effect their changes had.

[Here is a minimal example](/docs/tutorial/minimal-example.md)

