# v5 recording review

**File:** `Audition - Akmal Khan - Code Review with Codex v5.mp4`  
**Verdict:** Keep the slides and the demo story. Record the voice once more before submitting. The lesson is intact. Several words the lesson depends on do not come through, and the live demo is short of the kit's 3-minute floor.

Measured from the file on 25 Oct 2026. Words come from an English transcription. A word the transcriber was unsure of is treated as unclear, not as a quote.

## Snapshot

| Check | Result |
|---|---|
| Runtime | 7:27 (446.7 s). Inside the 5–8 minute kit. About 30 s of room under 8:00. |
| Picture | 1920×1080, 30 fps, H.264 |
| Audio | AAC, 48 kHz, stereo, both channels identical (mono voice, duplicated) |
| Loudness | −19.2 LUFS integrated. Peak −2.9 dBFS. No clipping. |
| Noise | Room tone near −55 dBFS. Rumble louder than hiss. |
| Level | Each minute of speech sits near −20 LUFS. Volume does not drift. |
| Longest mute | 6.9 s after "just as we planned" (about 6:09–6:16), digital silence near −100 dBFS |
| Live demo | 2:11 (4:11–6:22). Kit asks for 3–5 minutes. |
| Pace | About 140 words/minute overall. First three minutes about 150, pauses included. |

## Where the time goes

| Section | Clock | Length | Kit window | Reading |
|---|---|---|---|---|
| Overview (slides 1–3, through "let's make this real") | 0:00–1:09 | 1:09 | 60–90 seconds | Inside the window |
| Concepts | 1:09–4:11 | 3:01 | 2–5 minutes | Inside the window |
| Live demo (Codex app, through "ready to commit") | 4:11–6:22 | 2:11 | 3–5 minutes | About 50 seconds short |
| Close (comparison, habit, summary) | 6:22–7:27 | 1:06 | Under 1 minute | Six seconds over |

Words per minute by clock minute, pauses included: 151, 152, 150, 143, 128, 114, 140, 139. The dip at 4:00 and 5:00 is demo waiting, not a slower voice. The v8 script was written for about 140 words a minute.

## What already works

- The hook is up by 0:05 and the name by 0:08.
- The PR slide at 1:20 still shows the code and the green checks, and holds "Hold that thought" until the question is asked.
- The two-hats slide builds with the narration.
- The comparison slide and the summary do the close cleanly.
- Demo frames to keep: the boxed "3 findings: 2 × P1, 1 × P2" around 4:50, and the green "Clean re-review" box around 6:12.
- Almost no um or uh. The misses are diction, not hesitation.
- No clipping, stable loudness, correct delivery format.

## Lines to record again

| Time | What came through | Say it this way |
|---|---|---|
| 0:08 | "senior first tech AI architect" | Senior Full Stack AI Architect. Hit Full Stack. |
| 0:47 | "even that code still about 30" | Reviewing that code? Still about thirty. |
| 1:32 | "Not the ones what we forgot." | Not what we forgot. |
| 1:41 | "Saturated, 2 a.m." | Saturday, 2 a.m. |
| 1:52 | "sport tickets" | Support tickets. |
| 2:05 | "a bug in protection" | A bug in production. The transcriber was fairly sure of "protection." |
| 2:30 | "weird both heads" / "switch heads" | Wear both hats. Switch hats. The metaphor only becomes clear at the close. |
| 2:49 | The third question becomes "et cetera." | Say "empty or huge." The card is already on screen. |
| 3:09 | "when the final is coming" and "the Codex code wrote" | When the findings come in. Here's the code Codex wrote. |
| 6:41 and 7:23 | "tests were gained," and a soft last word | The tests were green. Then a full "happy reviewing," plus one silent second. |

"Tests pass" is the least reliable repeated phrase in the demo. The transcript keeps hearing "test paths."

## Picture fixes

1. At about 5:40 the diff is cropped while the narration says the size is checked as the file is copied. The breadcrumb reads "hoto-take," the error string ends at "Avatar mus," and the line numbers jump. Widen or zoom that pane so `MAX_AVATAR_BYTES` and the full error are on screen.
2. Cut the 6.9 s hold after "just as we planned" to about two seconds. Leave a little room tone. The pause at 0:39 still has room tone around −56 dBFS, so the later mutes sound like a hole.
3. A faint pen, laser, and slide-navigation cluster sits at the bottom left of every slide. That is PowerPoint's slideshow toolbar. It is absent from the Codex footage. Hide it, or export the deck instead of screen-recording the show.

## Sound fixes

- Raise the voice about 3 dB. Target about −16 LUFS. Peak headroom is already there.
- High-pass near 80 Hz to thin the rumble. Compression is unnecessary.
- Do not mute pauses to digital silence.

## Before the next take

Record the voice again over this picture. Keep the slides. Slow down only on the words in the table above. Say the third review question out loud. Give the last line a tail. If time is added anywhere, add it on the three findings so the demo clears three minutes.
