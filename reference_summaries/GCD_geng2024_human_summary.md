# GCD — Grammar-Constrained Decoding (Geng et al., 2024)

**What it says in plain English:**
LLMs are bad at generating structured output (JSON, parse trees, entity lists) without fine-tuning. GCD uses formal grammars to block invalid tokens during generation. Previous work was task-specific; GCD shows a single grammar formalism works across many tasks. They introduce input-dependent grammars where the grammar changes based on the input.

**Key result:** Grammar-constrained LLaMA-33B beats task-specific fine-tuned models on information extraction and entity disambiguation, without any fine-tuning. On parsing, it guarantees valid output but doesn't match supervised accuracy.

**What they got right:**
- Unified framework argument: one formalism for many tasks
- Input-dependent grammars: the constraint adapts to the input
- Opinionated best practices section
- Honest limitations (API incompatibility, latency, empty-string issue)

**What they missed:**
- Grammar expressiveness: context-free grammars can't capture all constraints
- Tokenization issues: BPE tokenization creates ambiguity in grammar specification
- No semantic reasoning: grammar guarantees syntactic validity, not semantic correctness

**How it relates to DCA-Trie:**
GCD provides the formal grammar foundation that DCA-Trie extends. Where GCD constrains based on grammar rules (syntactic validity), DCA-Trie constrains based on KG ontology (semantic validity). GCD's input-dependent grammars are conceptually similar to DCA-Trie's TypeOracle — both adapt the constraint set based on the input. But TypeOracle uses KG metadata rather than formal grammars.

**Key insight to borrow:**
The "unified framework" argument: position DCA-Trie not as a KG-specific hack but as an instance of a general pattern (dynamic constrained decoding) applied to knowledge graphs.
