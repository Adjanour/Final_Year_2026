# Guide 1: Introduction — LLMs, Hallucination, and the Problem

## What This Section Covers
Why LLMs hallucinate, what KGQA is, and why existing constrained decoding methods are insufficient.

## Key Concepts

### 1. LLM Hallucination
- LLMs generate text autoregressively: $P(y_t | y_{<t}, x)$ — each token depends on all previous tokens
- They produce fluent but factually wrong answers (15-60% hallucination rate)
- **Scaling paradox**: Larger models hallucinate MORE convincingly, not less
- Hallucination types: intrinsic (contradicts source) vs extrinsic (unverifiable claims)

### 2. Knowledge Graph Question Answering (KGQA)
- A KG is a collection of triplets: (entity, relation, entity)
  - Example: (Marie Curie, award_received, Nobel Prize in Physics)
- KGQA = answer questions by traversing chains of verified triplets
- Multi-hop question: needs multiple connected triplets to answer
  - "Who is the spouse of the ex-president of USA?" → 2 hops

### 3. The Permissiveness Problem
- GCR (baseline) builds a KG-Trie before decoding: all valid paths from the question entities
- For a 3-hop question with average out-degree $d \approx 20$ and 3 question entities:
  - Total paths = $3 \times 20^3 = 24,000$ structurally valid paths
  - But only 1 leads to the correct answer
- The LLM must filter 23,999 irrelevant paths using its own knowledge — the same mechanism that causes hallucination

### 4. Constrained Decoding
- **Logit masking**: Before softmax, set logits of invalid tokens to $-\infty$:
  $$\tilde{P}(x_t) = \text{softmax}(\mathbf{h}_t + (1 - \mathbf{m}_t) \cdot (-\infty))$$
- $\mathbf{m}_t$ is a binary mask: 1 = valid token, 0 = invalid
- This forces the LLM to only generate tokens that correspond to real KG facts

## The Key Insight

| Method | Valid tokens depend on | Adaptation |
|--------|----------------------|------------|
| GCR/DoG | $f(G, E_q)$ — graph + entities only | Static (same trie for all steps) |
| **DCA-Trie** | $f(G, E_q, q, y_{<t})$ — adds question + partial output | Dynamic (adapts at each step) |

## If Asked

> **"What is the problem with GCR?"**
> "GCR admits all structurally valid paths, but most are semantically irrelevant. A 3-hop question can have 24,000 valid paths, only 1 correct. The LLM must filter the rest using the same internal knowledge that causes hallucination."

> **"What does DCA-Trie do differently?"**
> "It conditions the valid token set on the question and partial output, not just the graph structure. This prunes irrelevant paths before the LLM sees them."

## Practice
1. Why does constrained decoding use $-\infty$ instead of just removing tokens from the vocabulary?
2. What is the difference between intrinsic and extrinsic hallucination?
3. Calculate the number of paths for a 2-hop question with 2 entities and average out-degree 15.
