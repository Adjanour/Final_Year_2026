# Writing Guideline — DCA-Trie Thesis

A consolidated reference for writing and revising chapters in this thesis. Synthesises the rubric, prose guide, Chapter 2 revision notes, and typographic checklist into a single document. Read this before writing or editing any chapter.

---

## 1. Core Principle

Every paragraph must pass one test:

> **Would a researcher working on GCR, DoG, or constrained decoding stop to read this?**

If not, it is background or exposition. Cut it, shorten it, or move it to a footnote.

---

## 2. Argument Structure

### What each chapter must do

| Chapter | Job | Failure mode |
|---------|-----|--------------|
| **Ch. 1** | Construct the problem as instability in the field | Reads as a task list ("I will implement X") |
| **Ch. 2** | Enrich the problem by putting sources in conflict | Reads as a catalogue of papers ("Author X did Y. Its limitation is Z.") |
| **Ch. 3** | Present method as argument (conditions, not recipes) | Reads as a lab manual ("Step 1: do this. Step 2: do that.") |
| **Ch. 4** | Decouple constraint tightness from answer correctness | Reads as a results spreadsheet ("GCR got X%, DCA got Y%") |
| **Ch. 5** | State the field's changed belief | Reads as a summary ("We did X, Y, Z") |

### The one-sentence test

Before writing any paragraph, ask:

> **Who already believes something that this paragraph should make them stop believing, or believe less confidently?**

Name that person (a GCR researcher, a DoG researcher, a KGQA engineer) and that belief. If you cannot, the paragraph is exposition.

---

## 3. Chapter-Specific Guidance

### Chapter 1 — Introduction

- Open with the tension between structural faithfulness and contextual relevance, not with "LLMs hallucinate"
- The problem must be located *in the community*, not in you ("current frameworks don't do X", not "I wanted to explore X")
- Objectives must map 1:1 to unresolved tensions, not just list tasks
- Scope section is a value statement ("here is why X answers a different question"), not a disclaimer

### Chapter 2 — Literature Review

- Group papers by shared insight, not one paragraph per paper
- Never end a paragraph with "Its limitation is" / "The limitation is"
- Put sources in conflict, not sequence: "DoG's dynamism exposes what GCR's staticness costs"
- Table 2.1 must be read as an argument in prose: *"No cell has both columns marked Yes — that is Gap 1"*
- After every complex sentence, add a short one (under 12 words) with the implication

### Chapter 3 — Methodology

- Every design choice must answer "why *this*, not the obvious alternative?"
- State the tension between conditions: tightening for R can threaten P
- SIR must be justified as *necessary*, not just nice to have
- Complexity analysis is not decorative — state what the numbers are *for*
- Scope boundaries must be falsifiable predictions, not hedges

### Chapter 4 — Results & Discussion

- Structure follows conditions (F → R → P → v2 → efficiency), not experiment log order
- Confront the reproduction gap (80.9% vs published 92.6%) on the first page with a causal hypothesis
- State the central finding as tension: "14.5% path reduction but Hits@1 dropped 5%"
- FNR (Condition P) must be reported as a number, not implied
- v2's interrupted status must be disclosed as a limitation, not smoothed over
- Every table/figure must have prose explaining what it *proves*, not just what it shows

### Chapter 5 — Conclusion

- Restate the field's changed belief, not just what we did
- Future work is the next instability, not a wish list
- Limitations are evidence, stated with the same confidence as results

---

## 4. Prose Style Rules

### Things to avoid

| Pattern | Why | Fix |
|---------|-----|-----|
| Triadic lists ("faster, cheaper, more reliable") | LLM default; vary lengths | 2 items, 4 items, or trail into subordinate clause |
| Hedge-then-assert ("While X is true, Y") | Repeated scaffolding is a fingerprint | Sometimes just assert; hedge unevenly |
| Stock transitions ("Furthermore, Moreover, Additionally") | Deadly in bulk | Start with the claim directly |
| Empty intensifiers ("plays a crucial role") | Says nothing specific | Replace with the actual mechanism |
| Uniform paragraph shape (topic → 3 supporting → wrap-up) | Too regular | Mix 2-sentence and long paragraphs |
| Summary restates (last sentence rephrases first) | Adds nothing | Last sentence must advance or point forward |
| "It is worth noting that" | AI filler, always deletable | Delete the whole clause |
| "significantly" without numbers | Overused intensifier | Give a number or remove it |
| "Its limitation is" as paragraph ending | Most common AI autopsy phrase | Embed critique in the preceding claim |

### Things to do

- Vary sentence length on purpose. After a complex sentence, add a short one (under 12 words).
- Let some claims stand unhedged. If FNR is high and explains the drop, say "this explains the drop."
- Keep your own inconsistencies. Varying terminology across chapters is natural; total uniformity is a tell.
- Write your own topic sentences and evaluative sentences in your own words.

---

## 5. Typographic Cleanup (Mechanical Pass)

Run this last, after all content edits are final:

1. Find every em-dash — keep max 2-3 per page. Replace with comma, full stop, or parentheses.
2. Unify quote-mark style document-wide (curly is standard for LaTeX).
3. Paste each chapter into a plain-text editor; search `\u00A0` and `\u200B`; strip.
4. Search "not just," "not only," "but also" — rewrite most instances as plain declarative.
5. Convert bold-lead-in bullets to prose in Chapters 1-4 (keep in tables/appendices only).
6. Skim for stray arrows/symbols outside diagrams.
7. Final read-aloud pass per chapter.

---

## 6. LaTeX Conventions

### Citation commands
- `\citep{key}` — parenthetical: "(Luo et al., 2025)"
- `\citet{key}` — textual: "Luo et al. (2025)"
- Max 3 names in citation, all names in bibliography

### Cross-references
- Use `\label{}` and `\ref{}` for all figures, tables, equations, sections
- Equation labels: `eq:descriptive_name`
- Figure labels: `fig:descriptive_name`
- Table labels: `tab:descriptive_name`

### Figure and table conventions
- Bold captions: `\captionsetup[figure]{labelfont={bf},textfont={bf}}`
- Table captions: ragged-right, single-linecheck=off
- Figures must appear in the List of Figures with proper numbering
- Every figure/table must be referenced in prose before it appears

### Equation formatting
- Use `\begin{equation}` with `\label{}` for numbered equations
- Cross-reference with `\eqref{}` (auto-parenthesised)

---

## 7. Pre-Submission Checklist

- [ ] No "Its limitation is" / "The limitation is" as paragraph endings
- [ ] No "It is worth noting that" anywhere
- [ ] No triadic lists (all length 3)
- [ ] No "Furthermore" / "Moreover" / "Additionally" clusters
- [ ] Em-dashes: max 2-3 per page
- [ ] Semicolons: max 1 per page
- [ ] Bold-lead-in bullets removed from body prose
- [ ] Every table/figure has prose stating what it proves
- [ ] Chapter 4 confrontation of reproduction gap on first page
- [ ] All cross-references resolve (no undefined references on compile)
- [ ] Run `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex` with zero errors
- [ ] Plain-text pass strips `\u00A0` and `\u200B`

---

## 8. Revision Priority (When Time Is Short)

1. **Chapter 4** — This chapter decides whether anyone cares. Structure around F→R→P, state the tension explicitly.
2. **Chapter 2 §2.7** — Merge paper-per-paragraph entries into insight-driven paragraphs.
3. **Phrase-level cleanup** — Remove all AI-tell phrases across all chapters.
4. **Chapter 1** — Ensure instability is clear and objectives map to tensions.
5. **Chapter 3** — Tighten design-choice justifications and add the R-vs-P tension sentence.
6. **Typographic pass** — Mechanical cleanup last.
