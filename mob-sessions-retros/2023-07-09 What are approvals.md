# 2022-07-09

==========

# Goals

-   improve documentation: explain better what approval tests mean
-   to that end, we're practicing using the fizzbuzz kata -> shared understanding -> document
-   idea: choose your own adventure documentation

# retro of the fizz buzz kata

-   timer could have been longer, maybe 5m
-   no typist recap
-   approving incorrect results - confusing, but it works, useful; one of many workflow with approvals
-   because we approved, we were able to safely refactor the code - e.g. extracting the `fizzbuzz` function
-   event - after extracting fizzbuzz - we got `None` - was easy to find that out thanks to the test; and the very short feedback loop (incl running the tests in watch mode)

what is "approval tests"?

-   it _is_ the feedback loop; the ability to get the FB from what you're doing, how changes affect output, w/o having to re-run it all the time
-   `verify` - compare the result to the approved file
    -   matches perfectly - test passes
    -   difference - the reporter highlights the mismatch; test fails
        -   textual representation of what we're working on

what does the user need to do, in order to use approvals?

-   setup a test
-   optional - reporter
-   do we need to create the approved file ourselves?
    -   initially it's created automatically when we first run the test
    -   once we receive a result that we like - we alter the approved file to reflect this - iow we copy received to approved
