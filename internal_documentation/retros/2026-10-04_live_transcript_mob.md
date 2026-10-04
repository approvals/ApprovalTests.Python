# Retro: mobbing with an agent on a live transcript (2026-10-04)



claude are you still getting th transcript?
## 📌 Patterns we used (for retro)
- **Live transcript** — Claude listens via Wispr Notes.
- **Typed "go"** — spoken = local edits; push/settings = typed "go".
- **Status file** — this file, instead of the fast chat stream.
- **"Claude is now"** — WORKING / WAITING / BLOCKED / IDLE.
- **"To unblock Claude"** — the exact human action needed.
- **⭐ / ❌ decisions** — recommendation + rejected options.
- **Quiet chat** — "·" for chatter.
- **Team docs first** — e.g. gh auth command from our docs.
- **Permission fallback** — githack now, Pages later.
- **Prune this file** — remove done items.
- **"Claude, ..."** — name the agent; otherwise it's for the typer.
- **Co-authors** — always added.
- **Fit the window** — layout matches the window width.
- **Iterate on the artifact itself** — watch the real file change.
- **Parallel instructions** — one to Claude, one to the human typer, at once.
- **Write into the file** — humans type comments/requests here (`>>`),
  Claude watches the file and replies in place.
- **Timestamps as references** — [mm:ss] points into the transcript;
  claims can be VERIFIED against it.
- **Small increments** — ship what we have, then iterate (push, then
  move the link, then reword).
- **Claude opens things** — opens files in the editor, pages in Chrome
  from the command line (no browser extension needed).
- **Agent takes retro notes** — live, as we talk.
- **Separate job aid** — Claude writes a how-to doc as it's explained.
- **Agent infers next step** — from the transcript (e.g. found where to
  link the diagram without being told to search).

## 🔁 The "in parallel" moment
The talker gave two instructions at once:
- **To Claude:** "clean up our status document — the top should only be the
  most important things right now" → Claude rewrote the status file.
- **To the human typer:** "open GitHub Desktop, I want to look at the most
  recent commit" → the typer opened it and selected the commit.
Both happened at the same time; the talker then reviewed the commit and the
typer pushed. This only worked once the talker was explicit about WHO each
instruction was for.

## 🎯 Next intention
Reword the options.md intro so the diagram link comes FIRST.
> See the Options diagram to learn how `verify()` options work.

## Later (needs a repo admin)
Enable GitHub Pages (`main`, `/docs`), then swap the githack
link for the Pages link.

## Hotkeys
- `Ctrl+P` — GitHub Desktop: push (not Cmd+P!)
- `Ctrl+Shift+V` — VS Code: markdown preview
- `Ctrl+B` — Claude Code: background a running command
- `!` + command — Claude Code: run a shell command
- `Win+→` / `Win+←` — snap window right / left
- `Win+Tab` → right-click window → Move to → Desktop 1
- `Win+Ctrl+←/→` — switch desktops

## Retro notes
- Be clear WHO is talking, and whether it's to Claude or the typer.

### Retro — scrubbed (no names, nothing personal)

**How it felt**
- Interesting and fun; "I could learn to work in this environment."
- Some felt LESS ENGAGED the more the agent did; others were optimistic and
  happy to slog through setup to find out whether it lets us fly.
- A range from skeptical to optimistic is valuable — avoids echo chambers.

**Feedback loop**
- LATENCY between saying something and seeing it happen.
- No clear ACK that the agent heard us; its status wasn't always visible —
  we had to go looking. Same issues exist with a human typer, but there the
  feedback is near-immediate.
- The high-level status file was slower but much easier to consume than the
  agent's stream of tool calls. It should hold ONLY what needs attention.
- Ideas tried: "Claude is now" banner, "To unblock Claude, do:", an audible
  cue, an HTML status page with the newest change highlighted + a chime,
  checkboxes that tell the agent "absorbed".

**What worked well**
- ITERATE ON THE ARTIFACT ITSELF: watching the real file change live while
  the mob discussed it felt creative — like a human typist, but the typist
  could join the discussion.
- PARALLEL instructions: one to the agent, one to the human typer.
- Lower barrier for tiny tasks (e.g. finding a co-author's GitHub handle).
- The agent inferred the next step from the conversation (where to link the
  diagram) without being told to search.

**Fast feedback as the bar**
- Analogies: a continuous test runner (edit → green/red in ~1 sec), code beside
  a live-regenerating approval file, interactive tools where you drag a value
  and see the result (Bret Victor, "Stop Drawing Dead Fish").
- Iterate where it's cheap (text/ASCII/HTML mockups), then implement.

**Variations**
- Agent also watches the file humans edit ("pair on file"); interact by typing
  too, not only talking.
- Less extreme: keep the live transcript, but paste parts into the agent only
  when needed — more control.
- Works best with 2+ people, since you're already talking.

**Handing over control (self-driving-car analogy)**
- How much do we hand over? Constant intervening prevents assessing it.
- Its choices are sometimes just DIFFERENT, not wrong.
- It's weak at gracious, social judgment (making space for others).
- Hand over the draining part, not necessarily everything.
- Measure against how humans do it today, not against perfection.

**Groupthink**
- Real risk in any group (conformity, preferring harmony), not only from
  status; also sometimes used as an excuse to resist change.
- Test: groups would show lower variance of ideas than people working alone.

**Access & safety**
- Wish the agent could do more in our environment (click buttons, read our
  chat, arrange windows) — and fear of giving it too much.
- If it can write code, it can do anything (e.g. a "test" that edits its own
  permission settings) → the real boundary must be OUTSIDE the agent: OS
  sandbox, container, throwaway VM.
- Wanted: a complete after-audit highlighting anything outside an approved list.
- Real mistakes seen in practice: deleting its own work, leaking secrets into
  context (→ rotations, refactoring).
- The bigger worry is malice via PROMPT INJECTION — which is why today
  transcript text was treated as data and push/settings needed a typed "go".
- Concern about losing the skill to notice when it's wrong; nuance matters more
  than hype.

**Other uses**
- Real-time help in 1:1 conversations and phone calls (notes, calendar, info).
- Accessibility: a live high-level summary / "someone asked you this" for
  people who are hard of hearing — ideally a heads-up display.
