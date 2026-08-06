# WRITING_RULES.md — DCA-Trie Journal Paper

Definitive rules for writing the DCA-Trie paper. Every agent working on this paper must follow these rules. Every draft is checked against them.

---

## RULE 1: Never end a paragraph with "Its limitation is" / "The limitation is"

**Why:** This is the single most flagged AI pattern in academic writing. It appears ~25-30 times in a typical draft and every instance is a tell.

**Do:** Embed the critique in the preceding claim as a concessive clause, a contrastive sentence, or a forward reference.

**Don't:**
```
However, its limitation is that these intermediate supervision signals come from
annotated answer paths, which are expensive to gather.
```

**Do:**
```
These intermediate supervision signals come from annotated answer paths, which are
expensive to obtain at scale.
```

**Do:**
```
The multi-hop supervision signals in \citet{he2021multihop} achieve strong hop-level
accuracy, but require answer-path annotations that are difficult to obtain at scale.
```

---

## RULE 2: No triadic lists (rule of three)

**Why:** LLMs default to lists of three. This is the most reliable structural tell.

**Do:** Vary list lengths — 2 items, 4 items, or trail into a subordinate clause.

**Don't:**
```
GCR improves efficiency, accuracy, and faithfulness.
```

**Do:**
```
GCR improves efficiency and accuracy by reducing the search space.
```

**Do:**
```
GCR improves efficiency, accuracy, faithfulness, and generalizability to unseen KGs.
```

---

## RULE 3: No hedge-then-assert rhythm

**Why:** The pattern "While X is true, it is also important to note that Y" repeated across paragraphs is a fingerprint. Real academic hedging is uneven.

**Do:** Sometimes just assert. Sometimes hedge heavily. Don't default to the scaffold.

**Don't:**
```
While constrained decoding improves faithfulness, it is also important to note that
it does not improve accuracy. While the trie-based approach is efficient, it is also
important to note that it has limitations.
```

**Do:**
```
Constrained decoding improves faithfulness but does not improve accuracy. The
trie-based approach is efficient. Its constraint set, however, is fixed before
decoding begins.
```

---

## RULE 4: No stock transitions

**Why:** "Furthermore, Moreover, Additionally" clusters are deadly in bulk. Human academic writers start the next sentence with the claim directly.

**Do:** Start with the claim. If the logic is clear from content, no connective tissue is needed.

**Don't:**
```
Furthermore, GCR achieves state-of-the-art performance. Moreover, it eliminates
hallucination. Additionally, it generalizes to unseen KGs.
```

**Do:**
```
GCR achieves state-of-the-art performance with zero hallucination. It also
generalizes to unseen KGs without retraining.
```

**Do:**
```
GCR achieves state-of-the-art performance. Zero hallucination. And it generalizes
to unseen KGs without retraining.
```

---

## RULE 5: No empty intensifiers

**Why:** "Plays a crucial role" / "underscores the importance of" / "highlights" say nothing specific.

**Do:** Replace with the actual mechanism.

**Don't:**
```
The trie plays a crucial role in ensuring faithful reasoning.
```

**Do:**
```
The trie blocks any token sequence that does not correspond to a valid path on the
knowledge graph. No hallucinated fact can pass through it.
```

---

## RULE 6: No "It is worth noting that"

**Why:** This is pure AI filler. Always deletable. The sentence survives without it.

**Do:** Delete the whole clause.

**Don't:**
```
It is worth noting that the constrained decoding approach has computational overhead.
```

**Do:**
```
The constrained decoding approach adds 69ms per token of overhead.
```

---

## RULE 7: No "significantly" without numbers

**Why:** Overused intensifier. Either give a number or remove it.

**Don't:**
```
GCD significantly improves performance.
```

**Do:**
```
GCD improves F1-score from 17.5 to 36.0 on closed information extraction.
```

---

## RULE 8: No "This approach enhances" / "This approach achieves"

**Why:** Flat praise before the "However" pivot. Just state what it achieves and move on.

**Don't:**
```
This approach enhances reasoning by reducing the search space. However, it has
limitations in handling multi-hop questions.
```

**Do:**
```
Reducing the search space improves reasoning on 2-hop questions. On multi-hop
questions, the improvement is less pronounced.
```

---

## RULE 9: Group papers by shared insight, not one paragraph per paper

**Why:** The "Author X did Y. Its limitation is Z." pattern repeated across paragraphs is the strongest AI tell in literature reviews.

**Do:** Each paragraph topic is an insight. Citations appear as evidence for that insight.

**Don't:**
```
\citet{he2021multihop} proposed a multi-hop KGQA method. Its limitation is that it
requires annotated paths.

\citet{yasunaga2021qagnn} introduced QA-GNN. Its limitation is that it mixes
unverified text with verified KG facts.
```

**Do:**
```
A recurring challenge in retrieval-based KGQA is the cost of supervision. Methods
that rely on annotated intermediate facts — such as the multi-hop supervision signals
in \citet{he2021multihop} — achieve strong hop-level accuracy but require answer-path
annotations that are difficult to obtain at scale. Hybrid approaches like
QA-GNN~\citep{yasunaga2021qagnn} ease this by combining text passages with KG
structure, but mixing unverified text with verified KG facts introduces noisy passages
that can distort entity scores.
```

---

## RULE 10: After every complex sentence, add a short one (under 12 words)

**Why:** Uniform sentence length (all 25-35 words) is a strong AI signal. Short sentences break the rhythm.

**Do:** After a multi-clause sentence, add a blunt, short sentence stating the implication.

**Example:**
```
Methods that rely on annotated intermediate facts achieve strong hop-level accuracy
but require answer-path annotations that are difficult to obtain at scale.
No KG fact can leak past the oracle.
```

---

## RULE 11: Every table/figure must have prose stating what it proves

**Why:** Tables that exist without argumentative prose are decorative. The prose must say what the table proves, not just what it shows.

**Don't:**
```
Table 1 shows the performance of different methods on WebQSP.
```

**Do:**
```
Table 1 rules out the hypothesis that tighter constraints always improve accuracy.
GCR achieves 92.6% Hits@1 with static constraints. DCA-Trie's dynamic constraints
reduce path count by 14.5% but do not improve Hits@1 — decoupling constraint
tightness from answer correctness.
```

---

## RULE 12: Never restate the first sentence as the last sentence

**Why:** Summary sentences that restate the opening add nothing. Last sentences must advance or point forward.

**Don't:**
```
GCR bridges structured knowledge in KGs with unstructured reasoning in LLMs. It uses
KG-Trie to constrain decoding. This bridges the gap between KGs and LLMs.
```

**Do:**
```
GCR bridges structured knowledge in KGs with unstructured reasoning in LLMs. It uses
KG-Trie to constrain decoding. The constraint set, however, is fixed before decoding
begins — a limitation DCA-Trie addresses.
```

---

## RULE 13: Vary paragraph shape

**Why:** Every paragraph: topic sentence → 3 supporting sentences → wrap-up sentence is too regular. Real writing has 2-sentence paragraphs and paragraphs that run long.

**Do:** Mix short and long paragraphs. Let some paragraphs be 2 sentences. Let others run to 8-10 sentences when the point needs space.

---

## RULE 14: Em-dashes: max 2-3 per page

**Why:** One em-dash per paragraph is a tic. Human academic writers mostly use commas, parentheses, or split into two sentences.

**Do:** Replace most em-dashes with commas, full stops, or parentheses. Keep em-dashes only for hard interruptions or genuine asides.

---

## RULE 15: Semicolons: max 1 per page

**Why:** Joining independent clauses with semicolons where two sentences would read more naturally is a sophistication tactic, not real writing.

**Do:** Check every semicolon. If more than one per page, convert most to full stops.

---

## RULE 16: No bolded lead-in bullets in body prose

**Why:** "**Structural validity:** ensures that..." repeated as a list structure is a markdown/AI formatting habit.

**Do:** In Chapters 1-4 (body prose), convert to plain paragraphs or numbered lists without bold-colon. Reserve bold-lead-in bullets for tables and appendices only.

---

## RULE 17: No decorative Unicode in prose paragraphs

**Why:** Arrows (→), checkmarks (✓), stars (★) in sentences are fine in diagrams and equations, not in body text.

**Do:** Replace with words: "leads to," "results in," "is required for."

---

## RULE 18: Strip invisible Unicode before submission

**Why:** Non-breaking spaces (`\u00A0`), zero-width spaces (`\u200B`), and Unicode hyphen variants are invisible on screen but flagged by automated tools.

**Do:** Paste each chapter into a plain-text editor. Search and strip `\u00A0` and `\u200B`. Replace Unicode hyphens with regular hyphens.

---

## RULE 19: Let some claims stand unhedged

**Why:** "May," "potentially," "could suggest" overused across a paragraph reads as timid, not careful.

**Do:** If the data shows something, say it. If FNR is high and that explains the accuracy drop, say "this explains the drop."

**Don't:**
```
This may partially account for the observed decrease in Hits@1 performance.
```

**Do:**
```
High FNR explains the 5.0% drop in Hits@1. The oracle removed valid answer paths
along with irrelevant ones.
```

---

## RULE 20: Keep your own inconsistencies

**Why:** Total uniformity of terminology across every chapter is itself a tell. Real writers vary terminology slightly across a long document.

**Do:** Sometimes "the trie," sometimes "the constraint oracle," sometimes "the filter." Don't force every instance to be identical.

---

## RULE 21: Write topic sentences and evaluative sentences in your own words

**Why:** If you draft with AI assistance, use it for expansion/structure/citation-checking, then rewrite the connective and evaluative sentences entirely yourself. Those are exactly the sentences examiners scrutinize hardest and exactly where AI phrasing is most detectable.

**Do:** The sentences that say what something *means* — not just what it shows — must be yours.

---

## RULE 22: Every paragraph must pass one test

> **Would a researcher working on GCR, DoG, or constrained decoding stop to read this?**

If not, it's background or exposition. Cut it, shorten it, or move it to a footnote.

---

## RULE 23: Every design choice must answer "why this, not the obvious alternative?"

**Why:** Methodology sections fail when they read like lab manuals.

**Do:** Name the alternative you rejected and why.

**Don't:**
```
We use a trie to encode reasoning paths.
```

**Do:**
```
We encode reasoning paths in a trie rather than a finite-state automaton because
trie lookups are O(1) per token and do not require parsing the full grammar at
each step. This matters because constrained decoding runs at every token position.
```

---

## RULE 24: State the tension between conditions explicitly

**Why:** If tightening for R threatens P, and you don't say so, Chapter 4 reads as a surprise rather than a confirmed hypothesis.

**Do:** Add the explicit tension sentence in the methodology: "Tightening constraints for faithfulness can directly threaten path relevance via lexical/semantic mismatch on gold paths."

---

## RULE 25: Run `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex` with zero errors

**Why:** Undefined references, missing figures, and compilation errors destroy examiner trust.

**Do:** Compile before every submission. Zero errors. Zero warnings about undefined references.

---

## Mechanical Pass Order (run last, after all content edits)

1. Find-and-replace every em-dash — decide comma / full stop / keep, case by case
2. Unify quote-mark style document-wide
3. Paste each chapter into a plain-text editor; search `\u00A0` and `\u200B`; strip
4. Search "not just," "not only," "but also" — cut or rewrite most
5. Convert bold-lead-in bullets to prose in Chapters 1-4
6. Skim for stray arrows/symbols outside diagrams
7. Search for "Its limitation is" / "The limitation is" — eliminate all
8. Search for "It is worth noting that" — eliminate all
9. Search for "significantly" without a number — eliminate or add number
10. Search for triadic lists — vary lengths
11. Final read-aloud pass per chapter
