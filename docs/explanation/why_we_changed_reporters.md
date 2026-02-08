# Why we changed reporters

## When

v17.0.0, released February 2026

## Why

Reporters are highly dependent on 3rd-party diff tools. Keeping these consistent across multiple ApprovalTests languages meant that every project had a less-than-optimal list.

In standardizing this, we had to break some backwards compatibility.

## Breaking changes

While we kept `reporters.json` as a configuration file, we have removed everything from it. We're keeping it as an entry point for customization for backwards compatibility.

removing this will also change retrieving a class-based diff reporters by name with `GenericDiffReporterFactory.get("name")`

## new structure

There are three types of diff reporter classes now available: 

1. Use a specific diff tool, for example `ReportWithBeyondCompare3Windows`
1. Find the one that works on that operating system, for example `ReportWithDiffToolOnWindows`
1. Report with a diff tool regardless of operating system or version, for example `ReportWithBeyondCompare`

All of them start with `ReportWith` to make it easy to find in your editor's autocomplete.



