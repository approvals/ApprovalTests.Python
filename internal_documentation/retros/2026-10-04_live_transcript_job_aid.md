# Job Aid: Live-transcript mobbing with an agent
_(from Nitsan's explanation, 2026-10-04 [153:00])_

## Fastest path (works tomorrow)
Use the **same setup as Nitsan** and reuse Nitsan's repository.
Different tooling → you'll need to adapt.

## Key building block
A note-taker with **REAL-TIME access to the transcript**. This is rare —
most note-takers only give you the transcript after the meeting.
Wispr Flow does it, so Nitsan built around it.

## How it works
1. **Note-taker: Wispr Flow** (Mac) — has a note-taker that
   transcribes in REAL TIME and writes the transcript to a
   **local file on disk**.
2. **Simplest case — agent on the same machine:**
   tell the agent to watch that transcript file. Done. Nothing else needed.
3. **Agent on another machine** (like today): you must BROADCAST the
   transcript. Nitsan's tool (already built) broadcasts it over a
   tunnel and gives you a URL. Paste the URL into the agent's chat —
   the page itself contains agent instructions for joining, catching
   up, and monitoring the live transcript.

## Gotchas
- **Model matters.** In another mob, Sonnet 5 refused / was very hard to
  get to use the live transcript. Today Opus 5.5 worked.
- **Use a real domain, not an ngrok link.** Back then the share link was
  ngrok; the agent was wary of fetching it, and even after fetching it
  didn't want to monitor. Nitsan's own domain helps.
- **Safety checks.** Claude Code's auto mode blocked joining the note
  (looks like data exfiltration). Fix: add a permission rule or run in a
  mode where you approve the commands.

- **Note-taking limit.** Wispr Flow warned "5 more minutes" at ~2h55m —
  note-taking seems capped around 3 hours; may be resumable.

- **Context window.** After ~2.5 hours of following the transcript (plus
  the work), Claude was at ~377k of 1M tokens (38%) — fine for a full
  session.

## Then, in the agent session
- Ask it to keep a high-level **status file** and open it in an editor
  (narrow window, "Claude is now: …" at the top).
- Address it by name: "Claude, …".
- Decide which actions need a typed "go" (push, repo settings).

## Optional: two-way HTML status page
- Ask for an HTML status page: any layout, newest change highlighted,
  a chime on change, auto-refresh.
- For **two-way** (checkboxes / typing on the page reach the agent), ask
  the agent to run a **tiny local server** and monitor its events.
  Not heavy — but the agent won't do it unless asked; otherwise it's
  just an unmonitored HTML page.
  (Today: `mob_server.py` on localhost:8765, run under Monitor.)

## Open questions
- Link to Nitsan's repo? (may be public; otherwise ask Nitsan for access.)
- Windows equivalent of Wispr Flow's note-taker?
