# DoG — Decoding on Graphs (Li et al., 2024)

**What it says in plain English:**
DoG defines "well-formed chain" — a sequence of KG triples where each connects to the previous one — as the principle for faithful reasoning. The LLM generates these chains token by token, with constrained decoding enforcing that each step is a valid triple from the graph. The subgraph expands as reasoning proceeds.

**Key result:** Beats retrieval-based and agent-based methods on three benchmarks. Works with small open-source LLMs (8B). Training-free. But needs the full graph as input (context window issue).

**What they got right:**
- Clean concept definition (well-formed chain) that the entire method flows from
- Progressive subgraph expansion — the constraint set grows as reasoning proceeds
- Honest about context window limitation

**What they missed:**
- No semantic filtering: all valid triples are equally likely at each step
- The constraint is topological only (must connect to visited entities), not semantic (must be relevant to the question)
- No analysis of when beam search helps vs. hurts

**How it relates to DCA-Trie:**
DoG's progressive subgraph expansion is conceptually similar to DCA-Trie's dynamic constraint updating. But DoG expands based on topology (any triple touching visited entities), while DCA-Trie expands based on semantic relevance (TypeOracle gates). DCA-Trie is more selective, which should reduce irrelevant paths without sacrificing accuracy.

**Key insight to borrow:**
The idea of defining a principle (well-formed chain) and building the method around it. DCA-Trie should similarly define its principle (admissible paths) and show how TypeOracle enforces it.
