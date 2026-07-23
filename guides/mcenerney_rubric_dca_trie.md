# Writing Rubric: McEnerney's "Craft of Writing" for DCA-Trie / KG-Constrained Decoding

A self-assessment tool for Chapters 1–5. Not a style guide — a **value-detection instrument**.
Every section should pass a single test: *would a researcher working on GCR, DoG, or
constrained decoding stop what they're doing to read this paragraph?* If not, it's
background, not argument, and needs to move or die.

---

## 0. The One Question That Governs Everything

Before writing or revising any paragraph, ask:

> **Who already believes something that this paragraph should make them stop believing,
> or believe less confidently?**

If you can't name that person (a GCR-style researcher, a DoG-style researcher, someone
building a KGQA production system) and that belief ("static tries are fine because
structural faithfulness is the hard part," "tighter constraint = better accuracy," "SBERT
filtering is basically free"), the paragraph is exposition. Cut it or demote it to a
footnote/table.

---

## 1. Chapter 1 (Introduction) — Constructing the Problem

McEnerney's rule: don't summarize the field, **destabilize** it.

| Check | Field-specific instantiation | Pass criteria |
|---|---|---|
| Opens with instability, not definition | Does §1.1 open with "LLMs hallucinate" (definition) or with the *tension* between structural faithfulness and contextual relevance? | The KG-triplet example and hallucination-rate stat are fine as evidence, but the paragraph must be organized around a **claim that GCR/DoG readers currently hold and shouldn't** |
| Problem is located *in the community*, not in you | Reads as "current frameworks don't do X" not "I wanted to explore X" | No first-person discovery narrative ("I became interested in...") |
| Gap is falsifiable | §1.2's `W_val(t) = f(G, E_q)` vs `f(G, E_q, q, y<t)` reformulation | A reader could, in principle, disagree with your gap and say why — if they can't disagree, it isn't a claim |
| Objectives read as *resolutions to the gap*, not a task list | §1.3 objectives i–vi | Each objective should map 1:1 to a specific unresolved tension named in §1.2, not just "implement v1," "implement v2" |
| Scope section is a value statement, not a disclaimer | §1.6 | Reframe: not "here's what we didn't do" but "here's why doing X would answer a *different* question than the one we're posing" |

**Red flag specific to this thesis:** Chapter 1 currently earns its instability well
(Eq. 1.1 → 1.2 is a genuine reformulation). The risk is Chapter 4 not paying off that
setup — see §4 below.

---

## 2. Chapter 2 (Literature Review) — Enriching the Problem, Not Cataloguing It

McEnerney's sharpest test: **a literature review that could be reordered without losing
meaning has failed.** Every subsection should exist because removing it would leave a
gap in the *argument*, not a gap in *coverage*.

| Check | Field-specific instantiation | Pass criteria |
|---|---|---|
| Sources are put in conflict, not sequence | §2.5.3: GCR vs. DoG | Does the text say "GCR does A, then DoG does B" (chronology) or "DoG's topological dynamism *exposes* what GCR's staticness costs, but DoG's own indifference to semantics shows the fix isn't dynamism alone" (conflict)? Aim for the latter everywhere |
| Each related-work paragraph ends by naming what remains unresolved *for your specific problem*, not generically | Your existing pattern ("The limitation is...") | Good — keep this discipline. Check it never degrades into "future work could explore X" (too vague to count as instability) |
| Table 2.1 is read as an argument, not filed as an appendix | The Structural Faithfulness / Semantic Conditioning columns | In prose, before or after the table, explicitly say: *"No cell in this table has both columns marked Yes — that is Gap 1, stated structurally."* Don't let the table make the argument silently |
| §2.9 (Synthesis) is the chapter's real thesis statement | Three gaps | This section should be quotable on its own as "what Chapter 2 proved." If someone read only §2.9, they should be able to state your contribution accurately |
| No "safe" summary sentences | e.g. "Much work has been done in this area" | Delete on sight — zero information, zero instability |

**Value-vocabulary table for this domain** (use deliberately, don't overuse):

| Weak (flow) | Strong (value / instability) |
|---|---|
| "Furthermore, GCR also..." | "GCR's structural guarantee, however, is bought at the cost of..." |
| "Many methods have explored..." | "These methods share a single unexamined assumption:..." |
| "This shows that semantic similarity is useful" | "This reveals a boundary that no reviewed method crosses: soft ranking vs. hard admission" |
| "In summary..." | "What Chapter 2 establishes, and Chapter 3 must now resolve, is..." |
| "It is important to note that..." | *(usually deletable — check if the sentence survives removal)* |

---

## 3. Chapter 3 (Methodology) — Method as Argument, Not Recipe

McEnerney's line that applies hardest here: **methodology sections fail when they read
like a lab manual.** Yours mostly avoids this because Eq. 3.1–3.4 frame the method as
*conditions to be satisfied*, which is already argumentative structure. Tighten it further:

| Check | Field-specific instantiation | Pass criteria |
|---|---|---|
| Every design choice answers "why *this*, not the obvious alternative?" | v1 vs. v2 rationale (§3.6.1, §3.7.1) | Explicitly name the alternative you rejected and why (e.g., why not score every candidate path at every step from scratch — cost — and why that cost tradeoff is the actual design axis) |
| Conditions (F, R, P) are pre-registered as **possibly not jointly satisfiable** | §3.2.2 | Add the explicit tension sentence: tightening for R can directly threaten P via lexical/semantic mismatch on gold paths. This is the single highest-leverage sentence to add in the whole thesis — it converts your Ch.4 result from "surprising failure" into "confirmed hypothesis" |
| SIR is justified as *necessary*, not just *nice to have* | §3.4.1 | The paragraph should make it uncomfortable for a reader to keep using Hits@1 alone after reading it — that's the test of a good metric-justification section |
| Complexity analysis is not decorative | §3.6.3 | State what the complexity numbers are *for*: predicting where v2 will fail before you show the v2 results (compounding cost when |P| stays large at shallow hops) |
| Scope boundaries are falsifiable predictions, not hedges | §3.10 | Rewrite each "may not transfer well" as a specific, checkable claim (see prior conversation — e.g. threshold calibration stratification gap) |

---

## 4. Chapter 4 (Results & Discussion) — The Chapter That Decides Whether Anyone Cares

This is where McEnerney's framework is most punishing, because **results chapters are
where students revert hardest to "showing what I did."** The fix: organize Chapter 4
around the *conditions from Chapter 3*, not around the *methods you ran*.

| Check | Field-specific instantiation | Pass criteria |
|---|---|---|
| Structure follows the claims, not the experiment log | F → R → P → v2 → efficiency, in that order | Do NOT structure as "GCR results, then DCA-v1 results, then DCA-v2 results" — that's a lab notebook, not an argument |
| Reproduction gap is confronted, not buried | 80.9% vs. published 92.6% | Must be addressed in the first page of the chapter, plainly, with a causal hypothesis (sdpa vs flash-attn, entity linker version). Burying it in a footnote is the single fastest way to lose an examiner's trust |
| The central finding is stated as *tension*, not as a number | 14.5% path reduction + SIR↓ but Hits@1↓ 5.0% | Explicit sentence: "This is inconsistent with the premise, established in Chapter 2, that permissiveness alone drives error." Say it plainly — don't let the reader infer the tension from a table |
| FNR (Condition P) is reported as a number, not implied | Currently missing from your results doc | If FNR is high → clean causal story (Condition P failed, explains accuracy drop). If FNR is low but accuracy still drops → harder and more interesting result (beam competition / relevance-score noise), gets its own subsection |
| v2's "interrupted" status is stated as a limitation on the result, not smoothed over | 1,466/1,628 questions | An examiner who finds this in the raw data before you disclose it will discount everything else in the chapter |
| Discussion explains *what the finding forces the field to stop assuming* | §4.8 synthesis | The paragraph should be usable, near-verbatim, as your abstract's "results" sentence |
| No orphan tables | Every table/figure has ≥1 sentence stating what it proves, not just what it shows | "Table X shows..." is descriptive (weak). "Table X rules out explanation Y for the accuracy drop" is argumentative (strong) |

**The chapter's real job:** decouple two things the field currently treats as
correlated — *constraint tightness* and *answer correctness*. If your numbers show
that decoupling, that is the dissertation's contribution, independent of whether DCA-Trie
"wins." Say that explicitly rather than leaving the reader to conclude "the method didn't
work."

---

## 5. Chapter 5 (Conclusion) — Don't Downgrade to Summary

| Check | Pass criteria |
|---|---|
| Restates the *field's* changed belief, not just "what we did" | Should read as "Researchers working on KG-constrained decoding can no longer assume X" |
| Future work is framed as the *next instability*, not a wish list | "ORT-as-planner / oracle-as-verifier" should be framed as the tension your results expose, not a bonus idea |
| Limitations are owned in the same voice as the findings | No apologetic tone shift — limitations are just more evidence, stated with the same confidence as results |

---

## 6. Whole-Document Diagnostic (run this last)

1. **Highlight test.** Print Chapters 1, 2, and 4's opening two paragraphs. Highlight
   every instability/value word (*however, inconsistent, unresolved, contradicts,
   nonetheless, exposes, fails to account for*). If a page has none highlighted, rewrite it.
2. **Reorder test.** Could any two subsections of Chapter 2 swap places without damage?
   If yes, they're listed, not argued — add explicit forward/backward references that make
   the order load-bearing.
3. **Delete-the-table test.** For every table/figure, cover it and read the surrounding
   prose. If the prose still makes the argument without the table, the table is
   supporting evidence (good). If the argument disappears, the table was doing work the
   prose should be doing.
4. **Stranger test.** Would a DoG or RouterKGQA author, reading only Chapter 4, feel
   obligated to respond to your results in their own next paper? If the honest answer is
   "they'd skim it and move on," the framing — not the data — needs another pass.
5. **Abstract-extraction test.** Try to write your thesis abstract using only sentences
   that already exist in §1.2, §2.9, §3.2.2, and §4.8. If you can't, one of those sections
   isn't doing its structural job yet.

---

*This rubric is a diagnostic instrument, not a formatting checklist — it's meant to be
applied to drafts, not used to generate prose from scratch.*
