# AGENTS.md — DCA-Trie Journal Paper

**This file is the binding contract for every agent working on this paper.**
Read it before writing, editing, or reviewing any section. Non-compliance = the draft is rejected.

---

## 1. Project Identity

**Paper title:** Dynamic Context-Aware Tries for Knowledge Graph-Constrained Large Language Model Generation

**Authors:** Bernard Kirk Adjanor Katamanso, Erica Amonor, Joseph Osei Nyarko, Jessica Afua Etornam Nsafuah

**Target venue:** ACL / EMNLP / NeurIPS (top-tier NLP/AI venue)

**Core contribution:** DCA-Trie adjusts valid knowledge graph paths during LLM decoding using a TypeOracle, rather than fixing them at the start (as GCR does). This decouples constraint tightness from answer correctness.

**Codebase:** `/home/bernard/research/projects/graph-constrained-reasoning`

---

## 2. Reference Papers

Three canonical papers govern this paper's writing style. Read them before writing:

| Paper | File | Why it matters |
|-------|------|----------------|
| **GCR** (Luo et al., ICML 2025) | `papers/Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models.pdf` | Direct baseline. Method-as-argument structure. |
| **DoG** (Li et al., EMNLP 2024) | `papers/Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs through Generation of Well-Formed Chains.pdf` | Concept-first argumentation. Honest limitations. |
| **GCD** (Geng et al., ICLR 2024) | `papers/Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning.pdf` | Unified framework positioning. Opinionated best practices. |

**Sentence patterns and wording bank:** `reference_summaries/canonical_papers_analysis.md`

**Human-term summaries:** `reference_summaries/GCR_luo2025_human_summary.md`, `DoG_li2024_human_summary.md`, `GCD_geng2024_human_summary.md`

---

## 3. Writing Rules (ENFORCED)

**Full rules:** `guides/WRITING_RULES.md`

Every agent must follow these rules. Every draft is checked against them. Violations must be fixed before proceeding.

### Absolute prohibitions (never do these)

1. **Never end a paragraph with "Its limitation is" / "The limitation is"**
2. **Never use triadic lists** (lists of exactly 3 items)
3. **Never use "It is worth noting that"**
4. **Never use "Furthermore, Moreover, Additionally" clusters**
5. **Never use "significantly" without a number**
6. **Never use "This approach enhances" / "This approach achieves" as flat praise**
7. **Never restate the first sentence as the last sentence**
8. **Never use bolded lead-in bullets in body prose** (Chapters 1-4)
9. **Never use decorative Unicode symbols in prose paragraphs**
10. **Never leave invisible Unicode characters** (`\u00A0`, `\u200B`)

### Required patterns (always do these)

1. **After every complex sentence, add a short one (under 12 words) with the implication**
2. **Every table/figure must have prose stating what it proves, not just what it shows**
3. **Every design choice must answer "why this, not the obvious alternative?"**
4. **Group papers by shared insight, not one paragraph per paper**
5. **Let some claims stand unhedged** — if FNR is high and explains the drop, say so
6. **Vary paragraph shape** — mix 2-sentence and long paragraphs
7. **Vary sentence length** — count words per sentence, break uniformity
8. **Keep your own inconsistencies** — terminology variation across chapters is natural
9. **Write evaluative sentences in your own words** — the sentences that say what something *means*
10. **Compile with `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex` with zero errors**

### Structural requirements

1. **Every paragraph must pass:** "Would a researcher working on GCR, DoG, or constrained decoding stop to read this?"
2. **State the tension between conditions explicitly:** "Tightening constraints for faithfulness can directly threaten path relevance"
3. **Limitations section:** honest, specific, falsifiable — not apologetic

---

## 4. Paper Structure

Follow the structure in `guides/dycat ppaper guide.pdf` (extracted to `/tmp/dycat_guide.txt`):

| Section | Pages | Key Content |
|---------|-------|-------------|
| Title, Abstract, Keywords | 1 | Strong title, 200-250 word abstract, 5-7 keywords |
| 1. Introduction | 3 | Background, motivation, problem statement, research gap, contributions, paper organization |
| 2. Related Work | 3-4 | Hallucination mitigation, KG reasoning, constrained decoding, prompt-based methods, comparison table |
| 3. Proposed Framework | 5-6 | Architecture, mathematical formulation, TypeOracle, DCA-Trie, SIR, algorithms, complexity |
| 4. Theoretical Analysis | 2-3 | Correctness, structural faithfulness, search-space reduction, oracle behavior |
| 5. Experimental Design | 2 | Datasets, baselines, metrics, RQs, hardware |
| 6. Experimental Results | 3-4 | Performance, runtime, memory, search-space reduction, SIR evaluation |
| 7. Extended Analysis | 2-3 | Ablation, oracle analysis, sensitivity, efficiency, robustness |
| 8. Discussion | 2-3 | Why results occurred, implications, limitations, comparison with literature |
| 9. Conclusion | 1 | Summary, contributions, limitations, future work |
| References | 3-5 | 60-100 references |

---

## 5. Key Results

| Method | Hits@1 | Hits@k | Path Reduction |
|--------|--------|--------|----------------|
| GCR_Baseline | 80.9% | 91.3% | — |
| DCA_v1_Static | 75.9% | 86.0% | 14.5% |
| DCA_v2_Dynamic | 53.5% | 53.5% | — (interrupted) |

**Configuration:** `rmanluo/GCR-Meta-Llama-3.1-8B-Instruct`, RoG-webqsp test, beam=10, group-beam, index_length=2, max_new_tokens=256, NVIDIA RTX 4090.

**Central tension to state explicitly:** 14.5% path reduction but Hits@1 dropped 5.0%. This decouples constraint tightness from answer correctness. Do not smooth this over — it is the paper's most important finding.

---

## 6. Key Equations

- Oracle specification: `W_val^DCA(t) = f(G, E_q, q, y^{<t})`
- SIR definition: `SIR = (1/|Q|) * SUM_q (1/L_q) SUM_{t=1}^{L_q} SIR(q,t)`
- TypeOracle: `is_admissible(r, e', answer_types, hop, max_hop) = type_gate AND range_gate`

---

## 7. Research Evolution

| | Approach 1 (Cosine) | Approach 2 (Decomposed) | Approach 3 (TypeOracle) |
|---|---|---|---|
| **Status** | Abandoned | Abandoned | **Final** |
| **Mechanism** | `cos(MiniLM(path), MiniLM(q))` | `ρ_r × ρ_e × ρ_traj` | Two ontology gates |
| **Why abandoned** | Single score can't distinguish type match from topical overlap; expensive | Still needs encoder; threshold persists | — |

**Must show this evolution in the paper.** Each abandoned approach is evidence for why the final design took the form it did.

---

## 8. Writing Sessions

| Session | Section | Status |
|---------|---------|--------|
| 1 | Title + Abstract + Keywords | Done — `paper/01_title_abstract_keywords.tex` |
| 2 | Introduction | Done — `paper/02_introduction.tex` |
| 3 | Related Work | Done — `paper/03_related_work.tex` |
| 4 | Proposed Framework | Done — `paper/04_proposed_framework.tex` |
| 5 | Theoretical Analysis | Done — `paper/05_theoretical_analysis.tex` |
| 6 | Experimental Design | Done — `paper/06_experimental_design.tex` |
| 7 | Results | Done — `paper/07_results.tex` |
| 8 | Extended Analysis | Done — `paper/08_extended_analysis.tex` |
| 9 | Discussion | Done — `paper/09_discussion.tex` |
| 10 | Conclusion | Done — `paper/10_conclusion.tex` |

**Protocol for each session:**
1. Read the relevant canonical paper section for tone calibration
2. Read the rules in `guides/WRITING_RULES.md`
3. Write the section
4. Run the rule checklist against the draft
5. Compile with `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex`
6. Verify zero errors

---

## 9. Reference Protocol

Before writing any section, find the relevant papers from `papers/`, read them with `pdftotext`, and create a one-paragraph human summary capturing:
- What they claimed
- How they proved it
- What they missed
- How it relates to DCA-Trie

Save summaries to `reference_summaries/`.

---

## 10. Style Calibration

**Openings should destabilize, not define.** Don't start with "LLMs hallucinate." Start with the tension between structural faithfulness and contextual relevance.

**Method reads as argument, not recipe.** Every design choice answers "why this, not the obvious alternative?"

**Results are stated as tension, not as numbers.** "14.5% path reduction but Hits@1 dropped 5%."

**Limitations are evidence, stated with the same confidence as results.** No apologetic tone shift.

**Future work is the next instability, not a wish list.**

---

## 11. Humanizing Rules

**From `guides/humanizing_prose_guide.md`:**

- No triadic lists
- No hedge-then-assert rhythm
- No stock transitions
- No empty intensifiers
- No uniform paragraph shape
- No summary restates
- No "It is worth noting that"
- No "significantly" without numbers
- No "Its limitation is" as paragraph ending
- Vary sentence length on purpose
- Let some claims stand unhedged
- Keep your own inconsistencies
- Write evaluative sentences in your own words

---

## 12. Pre-Submission Checklist

Before submitting any draft:

- [ ] No "Its limitation is" / "The limitation is" as paragraph endings
- [ ] No "It is worth noting that" anywhere
- [ ] No triadic lists (all length 3)
- [ ] No "Furthermore" / "Moreover" / "Additionally" clusters
- [ ] Em-dashes: max 2-3 per page
- [ ] Semicolons: max 1 per page
- [ ] Bold-lead-in bullets removed from body prose
- [ ] Every table/figure has prose stating what it proves
- [ ] All cross-references resolve
- [ ] Run `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex` with zero errors
- [ ] Plain-text pass strips `\u00A0` and `\u200B`

---

*This file is the binding contract. Every agent working on this paper must follow these rules. Every draft is checked against them.*
