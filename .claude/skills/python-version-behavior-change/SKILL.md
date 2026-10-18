---
name: python-version-behavior-change
description: Diagnose a failure that happens on only one Python version (often a new one). Use when tests pass on older Pythons but fail on a newer one, or vice versa.
---

# Check for a Python version behavior change

1. Narrow the pattern from CI: which Python version, and which OS? A single version on a single OS is a strong hint.
1. Read the "What's New" page for that version (https://docs.python.org/3.XX/whatsnew/3.XX.html) and its PEPs.
   Look for changed defaults, e.g.:
1. Confirm on an older Python by turning on the new behavior there, if a switch exists.
1. Fix the code so it doesn't depend on the default. Don't change approved files or test data just to make the test pass.
