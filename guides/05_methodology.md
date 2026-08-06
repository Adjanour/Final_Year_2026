# Guide 5: Methodology — The 4-Layer Architecture

## What This Section Covers

The system architecture, the four layers, and how they connect.

## The 4-Layer Architecture

```
Question: "Who is the spouse of the ex-president of USA?"
                          │
                          ▼
┌─────────────────────────────────────────────┐
│  Layer 1: Entity Linking                    │
│  Extract: USA, ex-president                 │
│  Map to KG: USA → entity:usa                │
└─────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────┐
│  Layer 2: Constraint Oracle (DCA-Trie)      │
│  TypeOracle gates prune irrelevant paths    │
│  v1: static filter  v2: dynamic expansion   │
└─────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────┐
│  Layer 3: Constrained Decoding              │
│  LLM generates with trie-masked logits      │
│  Only valid KG tokens have non-zero prob    │
└─────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────┐
│  Layer 4: Inductive Reasoning               │
│  GPT-4o-mini synthesizes answer from paths  │
│  Input: top K reasoning paths               │
│  Output: final answer                       │
└─────────────────────────────────────────────┘
```

## Layer-by-Layer Breakdown

### Layer 1: Entity Linking

- Input: Raw question text
- Output: Core entities mapped to KG nodes
- Example: "Who is the spouse of the ex-president of USA?" → {USA}
- Uses question-entity annotations from the dataset

### Layer 2: Constraint Oracle (OUR CONTRIBUTION)

- Input: KG subgraph, question entities, question text
- Output: Filtered set of valid paths
- **TypeOracle** applies two gates:
  - Range gate: every hop
  - Type gate: terminal hop only
- v1: Filters all paths before decoding (static)
- v2: Filters paths at each hop during decoding (dynamic)

### Layer 3: Constrained Decoding

- Input: LLM, trie, prompt
- Output: Generated reasoning path
- At each step:
  1. LLM produces logits over vocabulary
  2. Trie lookup returns valid next tokens
  3. Invalid tokens get $-\infty$ logit
  4. Softmax over remaining tokens
  5. Sample or beam search

### Layer 4: Inductive Reasoning

- Input: Top K reasoning paths from beam search
- Output: Final natural language answer
- Uses GPT-4o-mini to synthesize answer
- Example paths:
  - "USA → ex-president → G.W.Bush → spouse_of → Laura Bush"
  - "USA → ex-president → B.Obama → spouse_of → Michelle Obama"
- Answer: "Laura Bush, Michelle Obama"

## The Key Contribution: Layer 2

The DCA-Trie contribution is specifically in Layer 2. We're not changing the LLM, the decoding algorithm, or the reasoning step. We're changing HOW the constraint set is built.

## If Asked

> **"What is the system architecture?"**
> "Four layers: entity linking extracts question entities, the TypeOracle prunes the constraint set, constrained decoding forces the LLM to follow the trie, and inductive reasoning synthesizes the final answer from the top paths."

> **"Where is the DCA-Trie contribution?"**
> "In Layer 2 — the constraint oracle. We replace GCR's static trie with a TypeOracle that uses semantic gates to prune irrelevant paths before the LLM sees them."

## Practice

1. Why do we need Layer 4 (inductive reasoning) instead of just taking the last entity in the path?
2. What would happen if we removed Layer 2 entirely?
3. How does the constrained decoding layer enforce the trie constraint?
