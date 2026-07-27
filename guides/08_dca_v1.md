# Guide 8: DCA-Trie v1 — Static Filtering

## What This Section Covers
How v1 works, the algorithm, and its characteristics.

## How v1 Works

v1 filters paths BEFORE building the trie. It's a one-shot process:

```
Question → Enumerate ALL paths → Apply TypeOracle gates → Build trie from survivors
```

## Algorithm

```python
def dca_v1(data, oracle, index_len):
    # Step 1: Enumerate all paths from question entities
    graph = build_graph(data["graph"])
    entities = data["q_entity"]
    all_paths = dfs(graph, entities, index_len)  # e.g., index_len=2
    
    # Step 2: Infer answer types
    answer_types = oracle.infer_answer_types(data["question"])
    
    # Step 3: Apply TypeOracle gates to each path
    filtered_paths = []
    for path in all_paths:
        admitted = True
        for head, rel, tail in path:
            # Range gate: every hop
            if not oracle.range_gate(rel, tail):
                admitted = False
                break
        if admitted:
            # Type gate: terminal hop only
            terminal = path[-1][2]
            if not oracle.type_gate(terminal, answer_types, len(path), index_len):
                admitted = False
        if admitted:
            filtered_paths.append(path)
    
    # Step 4: Build trie from filtered paths
    trie = build_trie(tokenizer, filtered_paths)
    
    # Step 5: Run constrained decoding with this trie
    return constrained_decode(model, prompt, trie)
```

## Key Characteristics

| Property | Value |
|----------|-------|
| When filtering happens | Before decoding (offline) |
| Trie adaptation | None (static) |
| Complexity | $O(P \cdot L)$ where P = paths, L = path length |
| FNR | < 5% (by design) |
| SIR reduction | 85.5% on WebQSP |

## Path Reduction Example

**Question**: "Who is the spouse of the ex-president of USA?"

| Stage | Paths | Reduction |
|-------|-------|-----------|
| All DFS paths | 24,000 | — |
| After range gate | 20,400 | -15% |
| After type gate | 3,510 | -85.5% |
| Final trie | 3,510 | -85.5% total |

## v1 vs GCR

| Aspect | GCR | DCA-Trie v1 |
|--------|-----|-------------|
| Trie content | All valid paths | TypeOracle-filtered paths |
| SIR | 1.0 | 0.145 |
| Hits@1 | 91.6% | 86.4% |
| Latency overhead | — | +0.5% |
| Faithfulness | 100% | 100% |

## Why v1 Drops Accuracy

1. **Gold path exclusion**: TypeOracle occasionally removes the correct path (FNR = 3.3%)
2. **Beam competition**: Fewer paths means less diversity in beam search
3. **Regex noise**: Type inference is imperfect (85% accuracy)
4. **Precision-recall trade-off**: Tighter constraints reduce recall

## If Asked

> **"How does v1 work?"**
> "It enumerates all paths from the question entities, applies TypeOracle gates to filter out irrelevant paths, then builds a trie from the survivors. The LLM generates constrained by this filtered trie."

> **"Why does v1 drop accuracy?"**
> "Four reasons: gold path exclusion (3.3% FNR), beam competition (fewer paths = less diversity), regex noise in type inference, and the precision-recall trade-off."

> **"What is the latency overhead?"**
> "Only +0.5%. The TypeOracle gates are O(1) per candidate triple, so the total cost scales with the BFS frontier size, not path length."

## Practice
1. Why does v1 use DFS instead of BFS for path enumeration?
2. What would happen if we increased index_len from 2 to 3?
3. How does the trie lookup work during constrained decoding?
