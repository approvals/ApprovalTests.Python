# Introduction to Reporters

<!-- toc -->
## Contents

  * [What is a reporter](#what-is-a-reporter)
  * [Supported Diff Tools](#supported-diff-tools)
  * [resources](#resources)<!-- endToc -->

## What is a reporter
When approvaltests fails the mechanism to give you more information about that failing
is via a reporter. Most of the time this means opening a diff tool to show you 
the `.approved.` (expected) vs `.received.` (actual).  

The default reporter will search your machine for any installed diff tool.

## Supported Diff Tools  

* AraxisMergeMac <!-- include: GenericDiffReporterTests.test_document_existing_reporters.approved.md -->
* AraxisMergeWin
* BeyondCompare3
* BeyondCompare4
* BeyondCompare4Mac
* BeyondCompare4x64
* DiffMerge
* PyCharm
* diff
* kdiff3
* meld <!-- endInclude -->

## resources
1. [configuring a reporter]()
2. creating a custom reporter
3. Options
