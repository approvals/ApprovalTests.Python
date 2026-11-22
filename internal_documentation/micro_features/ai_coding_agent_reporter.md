# AI Coding Agent Reporter

Ported from the [ApprovalTests.Java micro feature](https://github.com/approvals/ApprovalTests.Java/blob/master/internal_documentation/micro_features/ai_agent_reporter.md).

`AiCodingAgentReporter` reports a failing approval as text on standard output when the tests are run by an AI coding agent.

## Purpose
AI coding agents can't see a diff tool that opens on the screen, but they can read console output. When an agent runs the tests, print everything it needs to understand and fix (or approve) the failure, instead of launching a diff tool.

## Detection
An agent is detected when any of these environment variables is set:

| Variable | Agent |
| - | - |
| `AI_AGENT` | generic opt-in |
| `APPROVAL_TESTS_AGENT` | generic opt-in |
| `CLAUDECODE` | Claude Code |
| `CLAUDE_CODE_ENTRYPOINT` | Claude Code |
| `CODEX_SANDBOX` | OpenAI Codex CLI |
| `CURSOR_AGENT` | Cursor |
| `CURSOR_TRACE_ID` | Cursor |
| `GEMINI_CLI` | Gemini CLI |
| `OPENCODE` | opencode |

A variable counts as set when it exists, is not blank, and is not a false value: `0`, `f`, `F`, `false`, `FALSE`, `False`. So `CLAUDECODE=0` lets a user opt out.

`AiCodingAgentReporter.ENVIRONMENT_VARIABLES` is a public, mutable list, so users can add an agent that is not listed.

## Behavior
`report(received_path, approved_path)`:
1. If no agent is detected, return `False`, so the next reporter in a `FirstWorkingReporter` gets a chance.
2. Otherwise print the report below to standard output and return `True`.

## Output
```
# APPROVAL TEST FAILED
    approved: /abs/path/foo.approved.txt
    received: /abs/path/foo.received.txt
    approve_with: mv -f /abs/path/foo.received.txt /abs/path/foo.approved.txt

    ## APPROVED
    ```txt
    hello world
    line two
    ```

    ## RECEIVED
    ```txt
    hello world
    line 2
    ```
----------------------
```
- Paths are absolute.
- `approve_with` comes from `get_command_text` in `clipboard_reporter.py`.

- If a file can't be read (for example, the approved file does not exist yet), its content is `** Error reading APPROVED file **` or `** Error reading RECEIVED file **`.

## Integration
Python gets a new front-loaded step, which runs before whichever reporter a test uses, including one the test names itself. It holds only `AiCodingAgentReporter`, so an agent never gets a diff tool it can't see.

`EnvironmentVariableReporter` moved there too, see [front_loaded_reporter.md](front_loaded_reporter.md).

It can also be used directly: `options=Options().with_reporter(AiCodingAgentReporter())`.
