# Introduction to Reporters

toc

## What is a reporter
When approvaltests fails the mechanism to give you more information about that failing
is via a reporter. Most of the time this means opening a diff tool to show you 
the `.approved.` (expected) vs `.received.` (actual).  

The default reporter will search your machine for any installed diff tool.

## Supported Diff Tools  

include: GenericDiffReporterTests.test_document_existing_reporters.approved.md

## resources
1. [configuring a reporter](https://github.com/approvals/ApprovalTests.Python/blob/main/docs/configuration.md#how-to-configure-a-default-reporter-for-your-system)
2. [creating a custom reporter]()
3. [Options]()
