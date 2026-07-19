# How to Use the IntelliJ Reporter

`ReportWithIntellijTools` automatically detects a running JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, GoLand, Rider, CLion, RubyMine, AppCode, or DataGrip) and uses its built-in `diff` command to display failed approval tests — no manual configuration required.

## Basic Usage

<!-- snippet: use_intellij_reporter -->
<a id='snippet-use_intellij_reporter'></a>
```py
class TestUseIntellijReporter(unittest.TestCase):
    def test_simple(self):
        verify("Hello", options=Options().with_reporter(ReportWithIntellijTools()))
```
<sup><a href='/tests/reporters/test_intellij_reporter.py#L16-L18' title='Snippet source file'>snippet source</a> | <a href='#snippet-use_intellij_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

`ReportWithIntellijTools` is also included first in the default `DiffReporter` chain, so if a supported IDE is running, it's picked automatically without any extra setup.

## Requirements

This reporter scans running processes to find the IDE, which requires the optional `psutil` dependency:

```bash
pip install psutil
```

If `psutil` isn't installed, or no supported JetBrains IDE is currently running, `ReportWithIntellijTools` reports itself as unavailable and the next reporter in the chain is used instead.
