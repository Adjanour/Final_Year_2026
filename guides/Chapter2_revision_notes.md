# Chapter 2 — Revision Notes

## What is working

The technical content is solid and the structure is logical. The synthesis section (§2.7,
Three Unresolved Gaps) is the strongest part of the chapter: it takes a position and
argues clearly. The figures and the summary table are well-chosen.

---

## The core problem: the "autopsy" paragraph pattern

Almost every paper in the Related Works section follows this exact three-sentence template:

> [Author] did X. [Positive claim]. [Its / The] limitation is Y.

Run a search for "limitation is" and "limitation of" — you will find this phrase appearing
approximately 25–30 times in the chapter, almost always as the final sentence of a
paragraph. AI detectors recognise this pattern immediately. So does any reader.

The fix is not to remove the critique — critical analysis is required. The fix is to
**vary where and how the critique appears**, and to **connect papers to each other**
rather than treating each one as an isolated case file.

---

## Section-by-section recommendations

### §2.1 Large Language Models (opening + subsections)

The intro paragraph is fine. The subsections are slightly textbooky — written as if
explaining LLMs to someone who has never heard of them. For an undergrad thesis in
this area, you can assume your reader knows what a transformer is. Tighten each
subsection to about half its current length.

**Specific fix — §2.1.2 Autoregressive Generation:**

Current:
> Since the generation condition includes all previously generated tokens, each new word
> becomes part of the context for the next word. [...] Importantly, because this
> distribution is always computed over the full vocabulary, any mathematically possible
> token has a positive, non-zero chance of being generated at any step.

The phrase "positive, non-zero chance" is redundant (positive already means non-zero).
Replace this paragraph with something like:

> Because each step conditions on all prior output, the process is self-reinforcing: a
> coherent but incorrect token at step $t$ produces a plausible context for step $t{+}1$,
> and the error propagates forward without correction. This is not a flaw that can be
> patched by better training data or larger models — it is a consequence of the
> generation mechanism itself.

This is shorter, makes the implication clear, and sounds like a person reasoning through
a problem rather than a textbook defining a term.

---

### §2.2 Hallucination

**§2.2.3 The Scaling Paradox** is well-argued and one of the more human-sounding
sections. Keep it largely as is. The reference to "inverse scaling" is a good detail.

One phrase to remove: "It is worth noting that" — this is a classic AI filler that adds
nothing and is easily flagged.

---

### §2.3 Multi-Step Reasoning

**§2.3.3 The Faithfulness Ceiling** is the best subsection in this section. It makes a
clean argument and ends on a strong claim. The subsections before it (§2.3.1 CoT and
§2.3.2 Extensions) read more like a textbook survey. Consider merging them into one
shorter section and spending the saved space strengthening the argument in §2.3.3.

---

### §2.5 Retrieval-Augmented Generation

The section is structured cleanly. The comparison figure (Figure 2.2) is good.

**§2.5.3 The Structural Limitation of Soft Grounding** makes the right argument. It
could be made punchier:

Current:
> Structural faithfulness with probability one, which guarantees that every generated
> token corresponds to a verified fact, cannot be achieved under any architecture that
> modifies only the input context without modifying the token selection mechanism.

Suggested (same argument, shorter):
> No matter how good the retriever is, faithfulness with probability one is unachievable
> without modifying the generation mechanism itself — because the model's output
> distribution is always computed over the full vocabulary, context or not.

---

### §2.7 Related Works — the section that most needs attention

This is by far the most AI-flagged section. Every subsection follows the same rhythm,
and the Retrieval-Based KGQA subsection (§2.7.2) is essentially a flat list of nine
paper summaries.

**Recommended structural change:**

Do not give every paper its own paragraph. Group papers by the insight they share, and
use the insight as the topic of the paragraph. Citations then appear as evidence for that
insight rather than as the subject of the sentence.

**Current approach (AI pattern):**
> \citet{he2021multihop} suggested a multi-hop KGQA method that learns intermediate
> supervision signals to guide path selection through the KG. [...] Yet, its limitation
> is that these intermediate supervision signals come from annotated answer paths, which
> are expensive to gather.
>
> \citet{yasunaga2021qagnn} introduced QA-GNN [...]. However, the joint graph mixes
> verified KG facts with unverified textual claims [...]

**Suggested approach (insight-driven):**
> A recurring challenge in retrieval-based KGQA is the cost of supervision. Methods
> that rely on annotated intermediate facts — such as the multi-hop supervision signals
> in \citet{he2021multihop} — achieve strong hop-level accuracy but require answer-path
> annotations that are difficult to obtain at scale. Hybrid approaches like
> QA-GNN~\citep{yasunaga2021qagnn} ease this by combining text passages with KG
> structure through a joint graph neural network, but mixing unverified text with
> verified KG facts introduces a new failure mode: noisy passages can distort entity
> scores derived from the graph structure.

Notice: same information, same citations, but written as an argument rather than a list.
The word "limitation" does not appear. The critique is embedded in the reasoning.

**Apply this principle throughout §2.7.** The most important subsections to revise:
- §2.7.2 Retrieval-Based KGQA (nine separate paper paragraphs → merge into 3–4
  insight-driven paragraphs)
- §2.7.4 Format-Constrained and Entity-Constrained Generation (ten paper paragraphs →
  merge into 3 groups: entity-level tries, grammar/FSM constraints, logic constraints)

---

## Phrase-level AI patterns to find and replace

Run a search for each of these. Every hit should be reworded.

| Pattern to remove | Why | Example replacement |
|---|---|---|
| `Its limitation is` | Most common AI autopsy phrase | Move the critique into the preceding claim |
| `The limitation is` | Same | Embed the critique as a concessive clause |
| `This approach enhances` | Flat praise before the "However" | Just state what it achieves and move on |
| `It is worth noting that` | AI filler | Delete or rewrite the sentence without it |
| `Despite their empirical improvements` | Formulaic pivot | "In practice, though," or "Even so," |
| `significantly` | Overused intensifier | Either give a number, or remove it |
| `in practice` + `in principle` (paired) | AI tending to cover all bases | Pick one or rewrite |
| Ending three consecutive paragraphs with `X cannot guarantee Y` | Pattern repetition | Vary the ending structure |

---

## Sentence-length variation

Read any paragraph in §2.7 aloud. The sentences are almost all the same length
(roughly 25–35 words). This is a strong AI signal. A simple fix: after every
complex, multi-clause sentence, add a short one (under 12 words) that states the
implication bluntly.

Example:

> [...] making trie lookups the most scalable option for applying firm factual
> constraints at inference speed~\citep{willard2023outlines}. **No KG fact can leak
> past the oracle.**

The short sentence breaks the rhythm and sounds like a researcher making a point,
not a system generating text.

---

## What NOT to change

- The formal definitions and equations are correct and should stay.
- The figures (kg_example, kg_trie_search, rag_vs_constrained) are good.
- The Three Unresolved Gaps section (§2.7 Synthesis) is the best-written part of the
  chapter. It takes a clear position and argues it directly. Use it as a style reference
  when revising the other sections.
- The summary table (Table 2.1) is well-structured and directly supports the synthesis.

---

## Priority order

If time is short, focus on these in order:

1. **§2.7.2 Retrieval-Based KGQA** — merge nine paragraph-per-paper entries into
   insight-driven paragraphs (biggest AI-pattern density, longest section).
2. **§2.7.4 Format-Constrained Generation** — same treatment, ten papers.
3. **Phrase-level find-and-replace** — remove all `Its limitation is` / `The limitation
   is` occurrences across the whole chapter.
4. **Sentence-length variation** — add short punchy sentences after complex ones in
   §2.2 and §2.3.
