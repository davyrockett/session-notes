# Session Notes

Record what happened in each Resounding Joy session, right after it, on your phone. Your Mac turns the
recordings into text, and Claude uses them to fill in the session forms once you approve a preview.

**Open it:** https://www.davyrockett.com/session-notes/ (or the Session Notes icon on your Apps screen)

## Using it

1. The list shows this week's sessions (and last week's). Your Mac fills it in every Monday morning.
2. Tap a session, tap the orange button, and talk: what you did from start to finish, how people responded and
   anything they said, and what you thought of it. Use initials, not names.
3. Tap again to stop. The recording is sent straight away. With no signal it stays on the phone and is sent the
   next time you open the app with a connection.
4. Remembered something else? Record again for the same session; they are combined.
5. A session that isn't on the list goes under **Another session**: say which session it is at the start.

Each session shows where it stands: **Not recorded**, **Waiting to send**, **Recorded**, or **Written up**.

## What happens to the recordings

- They go to a private project, `session-notes-data`, which only your access key can reach.
- When you say `/session-notes` to Claude on the Mac, it turns them into text (on the Mac itself, nothing is sent
  anywhere else), drafts each session form, and shows you a preview of the whole batch. It asks about anything
  it needs, and fills in the forms in Safari only after you approve.
- Once a form is submitted, that session shows **Written up** and its recordings are deleted from the private project.

## Settings (gear icon)

Appearance (Light / Dark / Auto), Access key, Share this app, and Check for updates.
The access key is the same one your other apps use; it must include the `session-notes-data` project.

## For changes

See `CLAUDE.md`. Test on the Mac with `Start Session Notes.command`.
