# Session Notes

Billing and documentation for each Resounding Joy session, right after it, on your phone. Your Mac turns the
recordings into text, and Claude uses them to fill in the session forms once you approve a preview.

**Open it:** https://www.davyrockett.com/session-notes/ (or the Session Notes icon on your Apps screen)

## Using it

1. The list shows this week's sessions (and last week's, plus any older week with something unfinished).
   Your Mac fills it in every Monday morning.
2. Tap a session, tap the orange button, and talk: what you did from start to finish, how people responded and
   anything they said, and what you thought of it. Use initials, not names. Tap again to stop. With no signal it
   stays on the phone and is sent when you're back online. Remembered something else? Record again.
3. Under **For billing**, fill in what you know: how many came, prep time, whether the times were as scheduled,
   and a note for the timecard (e.g. who observed). It saves as you go. Anything filled in here, you won't be
   asked about later.
4. **Winnetka**: the Winnetka row is for billing (tick who was there). Each resident has their own row below it
   for their own recording.
5. **+ Add other billable time** (bottom of the list) for time that isn't a session: hours and doc, band
   planning, prep, a meeting, drive time.
6. A session that isn't on the list goes under **Another session**: say which session it is at the start.

Each row shows where it stands: **Documentation** (not recorded, recorded, ✓ form submitted) and **Billing**
(no details, details added, ✓ on the timecard).

## What happens to the recordings

- They go to a private project, `session-notes-data`, which only your access key can reach.
- When you say `/paperwork` (or `/session-notes`) to Claude on the Mac, it turns them into text (on the Mac itself, nothing is sent
  anywhere else), drafts each session form, and shows you a preview of the whole batch. It asks about anything
  it needs, and fills in the forms in Safari only after you approve.
- Once a form is submitted, that session shows **Written up** and its recordings are deleted from the private project.

## Settings (gear icon)

Appearance (Light / Dark / Auto), Access key, Share this app, and Check for updates.
The access key is the same one your other apps use; it must include the `session-notes-data` project.

## For changes

See `CLAUDE.md`. Test on the Mac with `Start Session Notes.command`.
