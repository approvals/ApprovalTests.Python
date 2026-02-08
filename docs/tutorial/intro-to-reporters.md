# Introduction to Reporters

<!-- toc -->
## Contents

  * [What is a reporter](#what-is-a-reporter)
  * [Supported Diff Tools](#supported-diff-tools)
  * [Customizing the reporters.json](#customizing-the-reportersjson)
  * [resources](#resources)<!-- endToc -->

## What is a reporter

When an approval test fails, the mechanism to give you more information about that failing
is via a "reporter". Most of the time this means opening a diff tool to show you 
the `.approved.` (expected) vs `.received.` (actual).  

The default reporter will search your machine for any installed diff tool.

## Supported Diff Tools  

See [diff_reporters.csv](../../diff_reporters.csv) for a list of supported diff tools.

## Customizing the reporters.json

You can add a diff tool and path to ApprovalTests by editing the [`reporters.json`](../../approvaltests/reporters/reporters.json) file.

## resources
1. [configuring a reporter](../configuration.md#how-to-configure-a-default-reporter-for-your-system)
2. [creating a custom reporter](../how_to/create_a_custom_reporter.md)
4. [Options](../reference/options.md)
