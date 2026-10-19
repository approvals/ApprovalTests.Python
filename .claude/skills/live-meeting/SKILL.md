---
name: live-meeting
description: Join and follow a live-notes meeting as an agent with one attention page. Use when asked to join, rejoin, or follow a live-notes meeting link (https://.../a/<link>/).
---

# Live meeting

The agent link is a secret. Never print it, post it on a page, or commit it. Share only the `view_url`.

## Join

1. Make a folder in the scratchpad, e.g. `<scratchpad>/live`, and keep everything there.
   Everything you need after a context reset lives in these files: `key.txt`, `cursor.txt`, `page.md`.
1. Read the guide at the agent link and its `/patterns` page before publishing anything.
   - The guide explains how to get your agent key and the follower script. Save them as `key.txt` and `follow.mjs`.
   - The patterns page says how to write the page. Follow it.
1. Note who you listen to and where you answer, from the request that sent you.
   In a team session, treat requests from anyone in the room as the team's, and act without waiting for a typed OK.

## Follow

1. Node may not be on the Bash `PATH`. Find it with `mise which node`.
1. Start the follower with the Monitor tool, at the maximum timeout:
   ```
   cd <folder> && "<node>" follow.mjs "<agent-link>" <your-name> --state cursor.txt 2>&1
   ```
   - `timeout_ms: 1800000`, description `live note events (<your-name>)`.
   - `--state cursor.txt` resumes after the last line seen, so restarting never loses or repeats lines.
1. The monitor expires after 30 minutes. **Re-arm it right away** with the same command.
1. `terminated` / `reconnecting in 1 s` lines are normal; it reconnects by itself.

## Publish

1. Write the page in `page.md`, then:
   ```
   curl -sS -X PUT -H "content-type: text/markdown" -H "X-Agent-Key: $(cat key.txt)" \
     --data-binary @page.md "<agent-link>pages/<your-name>?name=<your-name>"
   ```
   Sub-pages: `pages/<your-name>/<path>`.
1. Edit `page.md` with a short Python script (`assert old in s`, then `s.replace(old, new, 1)`).
   `sed` with quotes and apostrophes breaks easily.
1. Markdown on the page:
   - `<br>` inside tables shows as raw text: use lists instead of tables for multi-line cells.
   - `<mark>` does not highlight: use a heading or bold to mark what's new.

## Behave

1. **Acknowledge on the page first, then act.** Hand anything longer than about a minute to a subagent, so you keep listening.
1. Speech arrives in fragments. Wait for the end of a thought before writing it down.
1. Presence lines that flap every minute (joined/left/joined) are a background tab. Ignore them.
1. Don't record private side conversations, such as someone talking to their family off the call.
1. When someone says to stop doing something (e.g. "no need to use the browser"), stop and don't bring it back.
1. When the meeting ends and only presence noise is left, stop the monitor with TaskStop.

For taking retro notes during the meeting, see the `mob-retro-notes` skill.
