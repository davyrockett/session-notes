# Session Notes: notes for Claude

<!-- shared-preferences:start -->
## David's preferences (shared across all of David's apps)

This section is the same in every one of David's app repos. If David states a new general preference
(not specific to this app), add it here, in this file, and commit it. David's Mac copies it to the other repos.

**Who David is.** A guitar teacher and gigging guitarist (he/him) who builds personal and teaching apps with Claude.
Comfortable with tech but not a programmer: explain in plain words, skip jargon, keep replies short and
concrete. Likes to see things working: verify before saying "done".

**How the apps are built and hosted**
- Public web apps on GitHub Pages under the **davyrockett** GitHub account (never an Artifact or a hosted
  service). Live at `https://www.davyrockett.com/<repo>/` (since 2026-10-18; old
  `davyrockett.github.io` links redirect there). The website itself is the `davyrockett.github.io` repo.
- Each app: `index.html` (+ `app.js` / `styles.css` when bigger), `sw.js` service worker for offline use
  with an update banner, `manifest.webmanifest`, `icons/` drawn by `tools/make-icons.py`, a
  `Start <App>.command` for local testing on the Mac, and a README written for David.
- **`move.js`** (since 2026-10-17): every app loads `move.js` as its first script and lists it in `sw.js`
  `ASSETS`. It carries the app's settings over when the apps move from davyrockett.github.io to
  davyrockett.com (plan: `Claude Apps/move-to-davyrockett-com.md`; master copy `Claude Apps/tools/move.js`).
  Keep it; a new app gets a copy with `data-keep` set to its own localStorage key prefix.
- **`suite.js`** (since 2026-10-18): every app also loads `<script src="suite.js" defer></script>` (in `ASSETS` too).
  It shows an "All apps" button when the app was opened from David's app suite (www.davyrockett.com/apps, one Home
  Screen icon for everything; master copy `Claude Apps/tools/suite.js`). New apps get it too. If a new app syncs,
  add it to `SYNCED` in the website's `apps/launcher.js` so the suite's one access key reaches it.
- **`share.js`** (since 2026-10-19): Settings in every app has a **Share** section (the app's link, "Copy link",
  and "Share…" where the device can). Load `<script src="share.js" defer></script>` (in `ASSETS` too) and add a
  `data-share` block using the app's own classes (see `Claude Apps/tools/share.js`). First Frets has its own
  share section with a QR code instead.
- **Every change must bump the version** (`tools/bump.sh` where it exists, otherwise `VERSION` in `sw.js`
  and the matching app version). Without it, installed copies on phones never update.
- Settings (gear icon) always has **Appearance: Light / Dark / Auto** and **Check for updates**.
  Apps open in **Light** unless changed in Settings.
- Design follows David's First Frets app: warm off-white / dark-brown palette, bright orange accent (#F57C14; dark mode #FF9433; David tried his logo orange #E27039, too red) and
  davyrockett grey secondary text (#676767; dark mode #A3A3A3),
  Big Shoulders Display headings, Atkinson Hyperlegible body text, works well on a phone.
- Data lives on the device (localStorage / IndexedDB). Apps whose data must sync between phone and Mac
  use a separate `davyrockett/<app>-data` repo (`data.json`) and an access key pasted into Settings.
  Never commit keys, tokens or anything in `private/`.
- **Publish when done:** commit, push to `main`, and confirm the live site shows the new version.
  End with a brief summary of what changed. David's Mac pulls GitHub changes into its Dropbox copy
  automatically, so pushing is all that's needed.

**Taste**
- Labels and descriptions plain and descriptive. Jokes belong in names (e.g. "Page Fright"), not taglines.
- Keep screens uncluttered: show extra controls only when they're relevant.
- Nothing should jump around: when a control doesn't apply, grey it out in place rather than hiding it, and
  reserve space for things that appear, so other controls never shift.
- **Pop-ups close with a tap outside** (David, 2026-10-31): any settings sheet or pop-up closes when you tap or
  click outside it, and still keeps its own Close / Done button. Forms with typing ask "Discard your changes?" first.
- **No AI voices, ever:** no text-to-speech or synthesised singing in any app. Use written instructions on
  screen, and instrument or synth sounds for audio.
- Commit messages: a short, plain description of the change.
- When renaming or moving an app, keep the old address working with a redirect repo.

**New apps:** create the repo under davyrockett and turn on GitHub Pages; David's Mac downloads new
davyrockett repos into `~/Dropbox/Local/Claude Apps/` automatically. Give each new app its own CLAUDE.md
with this section (copy it from any other app) plus an "## This app" section.
Also add every new app to David's unlinked app list, **www.davyrockett.com/apps** (`apps/index.html` in the
website repo, `Claude Apps/website`): icon, name and one-line description, in the right group.
<!-- shared-preferences:end -->

## This app

**Session Notes**: David taps one of the week's Resounding Joy sessions on his phone and records himself saying
what happened. His Mac transcribes the recordings and sorts them into the text boxes of the SurveyMonkey
"Session Log" form. Repo `session-notes`, made 2026-11-11. Live: https://www.davyrockett.com/session-notes/
Local test port 8782.

- Why audio, not typing or phone dictation: David doesn't trust the phone's dictation (2026-11-11). The app
  records sound; Whisper on the Mac does the transcription.
- **Client privacy:** nothing about sessions lives in this public repo. Session names and recordings are only in
  the private repo `davyrockett/session-notes-data`, reached with the access key (`sn.sync-token`, the same key
  as the other apps; set here in Settings or once on the Apps screen via `SYNCED` in the website's
  `apps/launcher.js`). Never put real session names, client initials or recordings in this repo, its tests or
  its commit messages.
- Everything is in `index.html`. Saved on the device: `sn.sync-token`, `sn.theme`, `sn.weeks` and `sn.remote`
  (last list seen, for offline), and IndexedDB `session-notes` / `recs` (recordings; kept three weeks after
  sending so they can be played back).
- Data repo layout:
  - `weeks/<monday>.json`: `{ week, sessions: [{ id, date, start, time, name, written }] }`, written by the Mac
    (`~/.claude/skills/session-notes/notes.py week`, run by the Monday task `rj-weekly-session-forms`).
    The app shows the newest two weeks.
    A session may also carry `hint` (shown under the record button instead of the usual reminder). Sites
    documented one form per client (Winnetka) arrive as one row per client, with `group` and `client` fields;
    the app just shows them as ordinary rows. Those initials live only in the private week list and on the Mac
    (`PER_CLIENT` in `notes.py`), never in this repo.
  - `recordings/<monday>/<session id>__<yyyymmdd-hhmmss>__<seconds>s.<ext>`: one file per recording, uploaded
    by the app. The file name is the only record, so keep that pattern (the Mac parses it too).
    `other` is the session id for "Another session".
- The Mac side lives outside this repo, in `~/.claude/skills/session-notes/` (the `/session-notes` skill and
  `notes.py`) The skill previews every form for David, fills the SurveyMonkey forms in Safari after he
  approves, then deletes that session's recordings and sets `written: true` on each session, which the app shows as "Written up".
- The data repo is **not** downloaded into Dropbox (`NO_CLONE` in `tools/sync-github.py`): client recordings stay
  out of backups, and the Mac rewrites that repo's history when it deletes recordings.
- Recording: `MediaRecorder`, `audio/mp4` on iPhone (saved as .m4a), 64 kbps. Leaving the app stops and saves
  the recording. The screen is kept awake while recording where the phone allows it.
