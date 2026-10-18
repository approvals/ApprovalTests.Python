---
name: read-ci-failure
description: Read why a GitHub Actions run or job failed. Use when CI is red, when given an actions/runs URL, or before trying to reproduce a CI failure locally.
---

# Read CI failure

Read the real CI log before forming any theory or reproducing locally.

1. Check the GitHub CLI login: `gh auth status`
   - If the token is invalid or missing, log in with the command from `internal_documentation/github_guidelines.md`:
   - It waits for the browser, so run it in the background and give the user the one-time code and URL it prints.
   - "HTTP 403: Must have admin rights to Repository" on log downloads usually means you are **not logged in**, not that you lack rights.
1. Find the failing jobs:
   - `gh run list --limit 10`
   - `gh run view <run-id> --json jobs -q '.jobs[] | "\(.conclusion) \(.name)"'`
   - Note the pattern: one OS? one Python version? all of them?
1. Read the failing job's log:
   - `gh run view <run-id> --job <job-id> --log-failed`
   - Search it for `FAILED`, `error`, `Traceback`, `×` (uv build failures).
1. Report the actual failing step and error message before proposing a cause.
   If you reproduce locally later, confirm the local failure matches this one.
