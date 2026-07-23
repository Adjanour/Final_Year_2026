# Typographic Tells: A Pre-Submission Cleanup Pass

This is separate from prose-style habits (see `humanizing_prose_guide.md`). These are
character- and formatting-level patterns — things you can literally find-and-replace —
that show up independent of what the sentence actually says, and are often what gets
flagged first, before anyone even reads for content.

Run this as a mechanical pass on the final draft, chapter by chapter, before binding/submission.

---

## 1. Em-Dash Overuse

The single most-cited giveaway. AI output defaults to "—" for parenthetical asides at a
much higher rate than typical academic prose, which mostly uses commas, parentheses, or
splits into two sentences instead.

- **Action:** Find every "—" in the document. For each one, ask: comma, full stop, or
  parenthesis instead? Keep an em-dash only where it's doing something a comma genuinely
  can't (a hard interruption or a genuine aside that needs stronger separation).
- **Target:** No more than 2–3 per page in flowing prose. Diagrams/equations are exempt.

## 2. Quote Mark Consistency

`" "` `' '` (straight) vs `" "` `' '` (curly/smart) — Word auto-curls quotes, but
pasted AI text sometimes carries a different style than the rest of the document, or
mixes both within a single document.

- **Action:** Pick one style (curly is standard for Word/LaTeX academic output) and
  find-and-replace to unify. Check especially any paragraph you copy-pasted from a
  chat window or PDF.

## 3. Invisible / Non-Standard Unicode Characters

Some pipelines insert characters that are invisible on screen but detectable in a
plain-text diff:

- Non-breaking space: `\u00A0`
- Zero-width space: `\u200B`
- Unicode hyphen variants: `‐` (U+2010) vs regular `-` (U+002D)
- Unicode minus sign: `−` (U+2212) vs hyphen `-`

- **Action:** Open the final draft in a plain-text editor (or paste into one) and
  search for `\u00A0` and `\u200B` specifically. Replace with regular spaces/hyphens.
  This matters more than it sounds — these are exactly the kind of artifact an
  automated similarity/AI-detection tool picks up on regardless of how the prose reads.

## 4. Semicolon Overuse as a "Sophistication" Tactic

Joining two independent clauses with a semicolon where two separate sentences would
read more naturally. Not wrong, but a noticeable pattern in bulk.

- **Action:** Skim for semicolons. If more than one per page, check whether each one
  earns its place or is just avoiding a full stop.

## 5. Bolded Lead-In Bullets in Flowing Prose

`**Structural validity:** ensures that...` repeated as a list structure. Very
recognizable AI/markdown formatting habit.

- **Action:** In Chapters 1–4 body prose, convert these into plain paragraphs or
  numbered lists without the bold-colon pattern. Reserve bold-lead-in bullets for
  genuinely tabular/reference material (tables, appendices) — not narrative argument.

## 6. Decorative Unicode Symbols in Body Text

Arrows (→), checkmarks (✓), stars (★) appearing in prose paragraphs rather than in
diagrams, equations, or tables.

- **Action:** Fine in Figures 3.1–3.4 and pipeline diagrams. If any appear inline in a
  sentence outside of an equation/diagram context, replace with words ("leads to,"
  "results in").

## 7. "Not X, but Y" / "Not Just X, But Also Y" Construction

A distinctive, repeatable AI sentence template. Fine once or twice in 90 pages, a tell
if it recurs every few paragraphs.

- **Action:** Search for "not just," "not only," "but also." Rewrite most instances as
  a plain declarative sentence instead.

## 8. Overly Perfect Oxford Comma / Style Consistency

Total, unbroken consistency in serial-comma use, hyphenation, or capitalization style
across 90 pages is itself an unusual signal — human writers drift slightly over a
long document, especially one drafted over months.

- **Action:** Nothing to "fix" here deliberately (don't fake inconsistency). Just don't
  be surprised if a detector treats too-perfect mechanical consistency as evidence —
  it's a real, known artifact of tool-assisted or tool-checked writing.

---

## Mechanical Pass Order (do this last, after all content edits are final)

1. Find-and-replace every em-dash — decide comma / full stop / keep, case by case.
2. Unify quote-mark style document-wide.
3. Paste each chapter into a plain-text editor; search `\u00A0` and `\u200B`; strip.
4. Search "not just," "not only," "but also" — cut or rewrite most.
5. Convert bold-lead-in bullets to prose in Chapters 1–4 (keep in tables/appendices only).
6. Skim for stray arrows/symbols outside diagrams.
7. Final read-aloud pass per chapter (catches rhythm issues the character-level pass won't).

Do this **after** the McEnerney-rubric pass and the prose-humanizing pass — this is the
last mechanical layer, not a substitute for the structural/argument work in those two.
