# GCR — Graph-constrained Reasoning (Luo et al., 2025)

**What it says in plain English:**
LLMs make things up when reasoning. Knowledge graphs have real facts. GCR converts the KG into a trie (prefix tree) and uses it to constrain what tokens the LLM can generate. The LLM literally cannot output a path that doesn't exist on the KG. They use a small fine-tuned LLM for constrained path generation, then a big LLM (ChatGPT) to pick the answer from multiple paths.

**Key result:** Zero hallucination in reasoning paths. 92.6% Hits@1 on WebQSP (vs 85.7% for previous best). Works on new KGs without retraining.

**What they got right:**
- Clean three-component architecture (trie → constrained decoding → inductive reasoning)
- Strong empirical results with honest ablation
- Zero-shot transferability demonstration

**What they missed:**
- Static trie: the constraint set is fixed before decoding starts, never adapts based on what the LLM has generated so far
- No semantic filtering: all paths within L hops are equally valid, even if irrelevant to the question
- No analysis of whether tighter constraints actually improve reasoning quality (they assume less hallucination = better answers)

**How it relates to DCA-Trie:**
DCA-Trie builds on GCR's trie-based approach but adds a TypeOracle that dynamically prunes paths based on semantic context during decoding. Where GCR's constraint is static (frozen trie), DCA-Trie's constraint adapts. This is the core contribution: moving from a fixed constraint to a context-aware one.

**Key equations to reference:**
- Eq. 6-7: Graph-constrained decoding formulation (constraint function CG)
- Eq. 8-10: Training loss and inductive reasoning over K paths
