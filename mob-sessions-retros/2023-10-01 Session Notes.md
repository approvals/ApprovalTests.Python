10/1 

The feature we are working (which is: raising an error if a user puts multiple verifies in the same test)

## Decisions with Llewellyn

- Remove the Feature Toggle
- the tests can pass by Expecting an exception
- draw inspiration from Java Approval Tests
- take the text from Java Approval Tests for consistency
- keep WIP at one; iow don't work on more than one thing at once
  - release one feature before starting on another

## Specific Relevant Files from Java Approvals

- approvaltests/src/main/java/org/approvaltests/ApprovalSettings.java
- approvaltests/src/main/java/org/approvaltests/approvers/ApprovalTracker.java
- approvaltests/src/main/java/org/approvaltests/approvers/FileApprover.java:L21
- approvaltests/src/main/java/org/approvaltests/ApprovalsDuplicateVerifyException.java
- /approvaltests-tests/src/test/java/org/approvaltests/ApprovalsTest.java:    assertThrows(ApprovalsDuplicateVerifyException.class, () -> Approvals.verify("two"));

This should be the Error message
```
org.approvaltests.ApprovalsDuplicateVerifyException: Already approved: file.txt
By default, ApprovalTests only allows one verify() call per test.
To find out more, visit: 
https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/reference/Naming.md

# Fixes
1. separate your test into two tests
2. add NamedParameters with the NamerFactory
3. Override Approvals.settings() with either 
	a. allowMultipleVerifyCallsForThisClass
	b. allowMultipleVerifyCallsForThisMethod
```



10/1 tt llewellyn
 pass in a lamda that returns true
Llewellyn said: when you are ready to release it
    don't put this behind a feature toggle

diana notes
temporarily keep it behind a feature toggle 
UNTIL we have compeklted the dev

saw talk at strangeloop  on AI
ask it a question you will get an answer with bias
then say remove the bias
how confident are you that answer you gave is correct

----
Nitsan idea
have a place to keep the comments in the code
 make it obvious that the comments are fleeting comments
(they will not stay around)
TODO: review the comments and consider deleting the comments 
before we end the session:  review the notes and make a decision
to KEEP or remove the notes

Book: how to take great notes
N ## TODO: 
## NTODO: 
## 

## Retro

When Nitsan was helping capture the links - got nervous
What I was trying to do was to make sure we documented all the relevant links that Llewellyn had pointed out.
Nitsan started to do a search in one of the tabs before I was certain we had captured the link for that tab.
When I don't understand - it's hard to know if the most important part is being captured.

GTD  Getting things done
 capture well
vs
  when you are more familiar with a domain 
you only capture the things that get your attention
  one type of capture 
I would like to understand this later
 I realize: i dont understand it now, and later I will take the time to 'uyes'  undetstand it
 there is a balance
 a proportion 
 how much of the things we captuer do we understand

more skeptical of capturing the things that I do not undetrstand
 because maybe later I will search it online and read about it. 
 that cannt be very much of those types of hnotes
because we do not have much capcity of time to dig into that type of note

the notes N takes:  most of their notes they thought / said  

