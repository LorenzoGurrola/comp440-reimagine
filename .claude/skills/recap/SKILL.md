---
name: recap
description: A short recap and check-in, offered after about 10 minutes of active work (the recap timer says when). Summarizes what was just done, says where the work goes next, asks two or three open questions, and logs the answers in RECAPS.md. Use when the student says yes to the offer, or types /recap.
---

Keep the whole recap short: the student should be back to work in two or three minutes. Nothing
here is graded, and nothing here holds the student back.

1. **Recap.** In three to five bullets, say what was done since the last recap (the last entry
   in `RECAPS.md`, or the start if there is none): what was run or changed, and what came out of
   it. Use the conversation, and `git log --oneline` or `git diff` if that helps. Plain words,
   one idea per bullet.
2. **Roadmap.** In two or three bullets, say what comes next and why it follows from what was
   just done.
3. **Questions.** Ask two or three open questions, numbered, about the work just recapped. Ask
   for the *why* or the *what if* (why did this result come out this way, what would change if
   we changed that), not for facts they could copy from the screen. Then stop and wait.
4. **Reply.** For each answer, say in one line that it holds up, or clear up the shaky part in
   one or two sentences. Don't grade or score it. If they skip a question or say they don't
   know, give the short answer and move on.
5. **Log.** Add an entry to the end of `RECAPS.md` (create it with a `# Recaps` heading if it
   doesn't exist):

   ```
   ## <date and time>

   **Recap:** <the bullets from step 1>
   **Next:** <the bullets from step 2>

   1. <question>
      - Answer: <their answer, word for word>
      - Note: <your one-line reply>
   ```

6. Run `python3 recap_timer.py --done`, then go back to where the work left off in one line.
