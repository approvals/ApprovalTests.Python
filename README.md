# ApprovalTests.Python

<!-- toc -->
## Contents

  * [What can I use ApprovalTests for?](#what-can-i-use-approvaltests-for)
  * [Getting Started](#getting-started)
    * [What Are Approvals](#what-are-approvals)
    * [New Projects](#new-projects)
      * [Minimal Example Tutorial](#minimal-example-tutorial)
    * [Adding to Existing Projects](#adding-to-existing-projects)
  * [Overview](#overview)
    * [Example using pytest](#example-using-pytest)
    * [Example using unittest](#example-using-unittest)
    * [Example using CLI](#example-using-cli)
      * [Usage](#usage)
      * [Argument Definitions](#argument-definitions)
  * [Reporters](#reporters)
  * [Support and Documentation](#support-and-documentation)
    * [Missing Documentation?](#missing-documentation)
    * [Dependencies](#dependencies)
      * [Python](#python)
      * [Required packages](#required-packages)
      * [Extra packages](#extra-packages)
  * [For developers](#for-developers)
    * [Weekly Ensemble](#weekly-ensemble)
    * [Pull Requests](#pull-requests)<!-- endToc -->

Capturing Human Intelligence - ApprovalTests is an open source assertion/verification library to aid testing.  
`approvaltests` is the ApprovalTests port for Python.

For more information see: [www.approvaltests.com](http://approvaltests.com/).

[![PyPI version](https://img.shields.io/pypi/v/approvaltests.svg)](https://pypi.org/project/approvaltests)
[![Python versions](https://img.shields.io/pypi/pyversions/approvaltests.svg)](https://pypi.org/project/approvaltests)
[![Build Status](https://github.com/approvals/ApprovalTests.Python/workflows/Test/badge.svg?branch=master)](https://github.com/approvals/ApprovalTests.Python/actions)
[![Build Status](https://github.com/approvals/ApprovalTests.Python/workflows/on-push-do-doco/badge.svg)](https://github.com/approvals/ApprovalTests.Python/actions?query=workflow%3Aon-push-do-doco)
[![Build Status](https://github.com/approvals/ApprovalTests.Python/workflows/Upload%20Python%20Package/badge.svg)](https://github.com/approvals/ApprovalTests.Python/actions?query=workflow%3A%22Upload+Python+Package%22)
[![Discord](https://img.shields.io/discord/1349240939406819409?logo=discord)](https://discord.gg/XDrgy6x6Se)

## What can I use ApprovalTests for?

You can use ApprovalTests to verify objects that require more than a simple assert including long strings, large arrays,
and complex hash structures and objects. ApprovalTests really shines when you need a more granular look at the test
failure. Sometimes, trying to find a small difference in a long string printed to STDOUT is just too hard!  
ApprovalTests solves this problem by providing reporters which let you view the test results in one of many popular diff
utilities.

## Getting Started

### What Are Approvals

If you need to gain a better understanding or are new to this concept, start [here](https://github.com/approvals/ApprovalTests.Documentation/blob/main/explanations/what_are_approvals.md).

### New Projects

If you are starting a new project, we suggest you use the [Starter Project](https://github.com/approvals/ApprovalTests.Python.StarterProject).
You can just clone this and go. It's great for exercises, katas, and green field projects.

#### Minimal Example Tutorial

If this is first time approvaltesting in python, consider starting here: [Minimal Example Tutorial](docs/tutorial/minimal-example.md)

### Adding to Existing Projects

From [pypi](https://pypi.org/project/approvaltests/):

    pip install approvaltests

## Overview

Approvals work by comparing the test results to a golden master. If no golden master exists you can create a snapshot
of the current test results and use that as the golden master. The reporter helps you manage the golden master.  
Whenever your current results differ from the golden master, Approvals will launch an external application for you to
examine the differences. Either you will update the master because you expected the changes and they are good,
or you will go back to your code and update or roll back your changes to get your results back in line with the
golden master.

### Example using pytest

<!-- snippet: getting_started_with_pytest.py -->
<a id='snippet-getting_started_with_pytest.py'></a>
```py
from approvaltests.approvals import verify


def test_simple() -> None:
    result = "Hello ApprovalTests"
    verify(result)
```
<sup><a href='/tests/examples/getting_started_with_pytest.py#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-getting_started_with_pytest.py' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Install the plugin pytest-approvaltests and use it to select a reporter:

    pip install pytest-approvaltests
    pytest --approvaltests-use-reporter='PythonNative'

The reporter is used both to alert you to changes in your test output, and to provide a tool to update the golden
master. In this snippet, we chose the 'PythonNative' reporter when we ran the tests. For more information about selecting
reporters see [the documentation](https://github.com/approvals/ApprovalTests.Python.PytestPlugin)

### Example using unittest

<!-- snippet: getting_started_with_unittest.py -->
<a id='snippet-getting_started_with_unittest.py'></a>
```py
import unittest

from approvaltests.approvals import verify


class GettingStartedTest(unittest.TestCase):
    def test_simple(self) -> None:
        verify("Hello ApprovalTests")


if __name__ == "__main__":
    unittest.main()
```
<sup><a href='/tests/examples/getting_started_with_unittest.py#L1-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-getting_started_with_unittest.py' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This example has the same behaviour as the pytest version, but uses the built-in test framework `unittest` instead.

### Example using CLI

You can invoke a verify() call from the command line. This allows invoking python approvals from any other stack via subprocesses.

#### Usage

```
python -m approvaltests --test-id hello --received "hello world!"
```

or

```
python -m approvaltests -t hello -r "hello world!"
```

or

```
echo "hello world!" | python -m approvaltests -t hello
```

#### Argument Definitions

-   **`--test-id`** or **`-t`**: Test identifier used to name the `approved.txt` and `received.txt` files for the test.

-   **`--received`** or **`-r`**: The output of the program under test (a string) that is passed to the verify method.

    -   **`stdin`**: Instead of providing a `received` argument, you may use `stdin`.

## Reporters

A reporter controls how ApprovalTests handles a failing test result. 
The default behavior is to open a diff tool showing what you received vs what was approved. 
You can use this diff tool to change the approved to make the test pass the next time you run it.
Reporters also have more advanced usages.

- [Intro to reporters](/docs/introduction_to_reporters.md)
- [How to select a reporter](/docs/how_to/select_a_reporter.md)
- [How to create a custom reporter](/docs/how_to/create_a_custom_reporter.md)

## Support and Documentation

-   [Documentation](/docs/README.md)

-   GitHub: [https://github.com/approvals/ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python)

-   ApprovalTests Homepage: [http://www.approvaltests.com](http://www.approvaltests.com)

### Missing Documentation?

If there is documentation you wish existed, please add a `page request` to [this issue](https://github.com/approvals/ApprovalTests.Python/issues/135).

### Dependencies

#### Python

ApprovalTests is tested on the following Python versions: 3.10, 3.11, 3.12, 3.13, 3.14.<!-- singleLineInclude: tests/approved_files/test_workflow_matrix.test_tested_versions_message.approved.txt -->

For older versions of Python, either:
- use an older version of ApprovalTests, or
- use [TextTest](https://texttest.org/), or
- hire us to help

#### Required packages

These dependencies are always required for approvaltests

<!-- snippet: requirements.prod.required.txt -->
<a id='snippet-requirements.prod.required.txt'></a>
```txt
pytest>=8.0.0
empty-files>=0.0.3
typing_extensions>=4.12.0
```
<sup><a href='/requirements.prod.required.txt#L1-L3' title='Snippet source file'>snippet source</a> | <a href='#snippet-requirements.prod.required.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

#### Extra packages

These dependencies are needed if you are going to use the related functionality.  
If you want the bare minimum you can use the pypi project
[approvaltests_minimal](https://pypi.org/project/approvaltests-minimal/).

<!-- snippet: requirements.prod.extras.txt -->
<a id='snippet-requirements.prod.extras.txt'></a>
```txt
# For reporters.clipboard_reporter.ClipboardReporter
pyperclip>=1.5.29

# For approvals.verify_html()
beautifulsoup4>=4.9.0

# For pairwise_combinations.get_best_covering_pairs()
allpairspy>=2.1.0

# For utilities.logging.logging_approvals.verify_logging()
testfixtures >= 7.1.0, < 12
mock >= 5.1.0
```
<sup><a href='/requirements.prod.extras.txt#L1-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-requirements.prod.extras.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## For developers

### Weekly Ensemble

The best way to contribute is to [join our weekly mob/ensemble](./docs/Contribute.md).

### Pull Requests

Pull requests are welcomed, particularly those accompanied by automated tests.

To run the self-tests:
`./build_and_test.sh`

This will run the self-tests on several python versions. We support python 3.10 and above.

All pull requests will be pre-checked using GitHub actions to execute all these tests. You can see the [results of test
runs here](https://github.com/approvals/ApprovalTests.Python/actions).
