# How to Use Front Loaded Reporters

<!-- toc -->
## Contents

  * [What they are](#what-they-are)
  * [The default front loaded reporter](#the-default-front-loaded-reporter)
  * [Turn it off for one block of code](#turn-it-off-for-one-block-of-code)
  * [Replace it](#replace-it)<!-- endToc -->

## What they are

A front loaded reporter runs **before** any other reporter, including one you set with `options.with_reporter(...)`.
If it reports the failure, no other reporter runs. If it does not, the normal reporter runs as usual.

This is how ApprovalTests avoids opening a diff tool where nobody can see it, such as when an AI coding agent runs your tests.

## The default front loaded reporter

By default, these reporters are tried first, in order:

1. `EnvironmentVariableReporter`: reports when `APPROVAL_TESTS_USE_REPORTER` is set. See [Select a reporter via an Environment Variable](use_environment_variable_reporter.md).
2. `AiCodingAgentReporter`: reports as plain text when an AI coding agent (such as Claude Code, Codex, Cursor or Gemini CLI) is running the tests.

When neither applies, your normal reporter runs.

## Turn it off for one block of code

Use `disabled_front_reporter` when your own reporter must run, for example in a test that checks your reporter was called:

<!-- snippet: disabled_front_reporter -->
<a id='snippet-disabled_front_reporter'></a>
```py
with disabled_front_reporter():
    reporter = get_reporter(my_reporter)
```
<sup><a href='/tests/reporters/test_front_loaded_reporter.py#L67-L70' title='Snippet source file'>snippet source</a> | <a href='#snippet-disabled_front_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Replace it

Set your own front loaded reporter for the current thread.
It should return `False` from `report` when it does not apply, so the normal reporter can run:

<!-- snippet: set_front_loaded_reporter -->
<a id='snippet-set_front_loaded_reporter'></a>
```py
set_front_loaded_reporter(my_ci_reporter)
```
<sup><a href='/tests/reporters/test_front_loaded_reporter.py#L78-L80' title='Snippet source file'>snippet source</a> | <a href='#snippet-set_front_loaded_reporter' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Pass `None` to turn front loading off.
