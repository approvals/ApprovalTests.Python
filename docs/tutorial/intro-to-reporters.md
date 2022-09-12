# Introduction to Reporters

<!-- toc -->
## Contents

  * [What is a reporter](#what-is-a-reporter)
  * [Supported Diff Tools](#supported-diff-tools)
  * [Customizing the reporters.json](#customizing-the-reportersjson)
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
* kdiff3
* meld <!-- endInclude -->

## Customizing the reporters.json

You can add a difftool and path to ApprovalTests by editing the [`reporters.json`](../../approvaltests/reporters/reporters.json) file.

## resources
1. [configuring a reporter](../configuration.md#how-to-configure-a-default-reporter-for-your-system)
2. [creating a custom reporter](../how_to/create_a_custom_reporter.md)
4. [Options](../reference/options.md)
