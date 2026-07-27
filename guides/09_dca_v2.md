# Guide 9: DCA-Trie v2 — Dynamic Expansion

## What This Section Covers
How v2 works, the hop-by-hop algorithm, and why it's more aggressive than v1.

## How v2 Works

v2 expands the trie step-by-step as entities are committed. It's a dynamic process:

```
For each hop:
  1. Enumerate gated paths from current head entities
  2. Build per-beam trie from surviving paths
  3. LLM generates ONE hop constrained by this trie
  4. Update head pool with newly committed entity
```

## Algorithm

```python
def dca_v2(data, graph, model, tokenizer, oracle, max_hops):
    # Phase 1: Initialize beams from first-hop gated paths
    initial_beams = []
    for entity in data["q_entity"]:
        first_hop_paths = get_gated_paths(graph, entity, oracle, ...)
        if first_hop_paths:
            initial_beams.append(BeamUnit(sequence=prompt, head_pool={entity}))
    
    # Phase 2: Iterate hops
    current_beams = initial_beams
    for hop in range(1, max_hops + 1):
        new_beams = []
        for beam in current_beams:
            # Step 1: Topological enumeration + semantic pruning
            allowed_paths = []
            for head in beam.head_pool:
                paths = get_gated_paths(graph, head, oracle, ...)
                allowed_paths.extend(paths)
            
            if not allowed_paths:
                continue  # Dead end — no backtracking
            
            # Step 2: Build per-beam trie
            trie = build_trie(tokenizer, allowed_paths)
            
            # Step 3: Constrained generation for ONE hop
            hop_prompt = f"{beam.sequence}\n<PATH>"
            output = model.generate(hop_prompt, trie, eos_token="</PATH>")
            
            # Step 4: Parse and update beam
            new_entity = extract_entity(output)
            new_beams.append(BeamUnit(
                sequence=beam.sequence + output,
                head_pool=beam.head_pool | {new_entity},
            ))
        
        # Keep top beams
        current_beams = sorted(new_beams, key=score, reverse=True)[:beam_size]
    
    # Phase 3: Extract answer from best beam
    return extract_answer(current_beams[0])
```

## v1 vs v2

| Aspect | v1 | v2 |
|--------|----|----|
| When filtering | Before decoding (offline) | During decoding (online) |
| Trie adaptation | None (static) | Per-hop (dynamic) |
| Head pool | All entities at once | Expands with each hop |
| Backtracking | N/A | No backtracking (DoG-style) |
| Complexity | $O(P \cdot L)$ | $O(L \cdot B \cdot d_{\text{avg}})$ |
| Accuracy | 86.4% Hits@1 | 54.0% Hits@1 |

## Why v2 Is More Aggressive

1. **Per-hop filtering**: Each hop gets its own TypeOracle check, not just the final path
2. **Head pool expansion**: New entities open up new paths that weren't available before
3. **No backtracking**: If a beam reaches a dead end, it's dropped permanently
4. **Beam competition**: Only top beams survive, reducing diversity

## Why v2 Drops Accuracy More

- **Aggressive pruning at each hop**: Errors compound — if hop 1 prunes the wrong path, hop 2 can't recover
- **No backtracking**: DoG-style means once you drop a beam, you can't go back
- **Beam collapse**: With fewer paths, beams converge to similar solutions

## If Asked

> **"How does v2 differ from v1?"**
> "v1 filters all paths before decoding. v2 filters at each hop during decoding, expanding the trie dynamically as new entities are committed."

> **"Why does v2 perform worse than v1?"**
> "v2 is more aggressive — it filters at each hop and doesn't allow backtracking. Errors compound: if hop 1 prunes the wrong path, hop 2 can't recover. v1's static approach preserves more diversity."

> **"What is the complexity of v2?"**
> "$O(L \cdot B \cdot d_{\text{avg}})$ — linear in hops, beams, and average degree. Much better than v1's $O(E^L \cdot L)$ exponential scaling."

## Practice
1. Why does v2 use beam search instead of greedy decoding?
2. What would happen if we allowed backtracking in v2?
3. How does the head pool prevent cycles?
