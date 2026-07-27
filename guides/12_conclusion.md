# Guide 12: Conclusion & Recommendations — What's Next

## What This Section Covers
The key takeaways, limitations, and future directions.

## Key Takeaways

### 1. TypeOracle Works (But Not How We Expected)
- SIR drops from 1.0 to 0.145 (85.5% improvement)
- FNR stays below 5% (design condition met)
- 100% structural faithfulness preserved
- **But**: Hits@1 drops by 5.2pp

### 2. Constraint Tightness ≠ Accuracy
- This is the non-monotone result
- Tighter constraints improve constraint quality (SIR) but NOT answer accuracy (Hits@1)
- Structural constraint quality and reasoning accuracy are distinct properties

### 3. SIR Enables Future Work
- First metric to measure constraint quality independently
- Enables systematic comparison of oracles
- Can be used to optimize constraints without conflating with accuracy

## Limitations

| Limitation | Impact | Future Fix |
|-----------|--------|------------|
| Freebase-only evaluation | May not generalize | Test on Wikidata, ConceptNet |
| Heuristic type inference | 85% accuracy | Use LLM-based type extraction |
| Limited schema coverage | 40 of ~24,000 Freebase relations | Extend relation-range coverage |
| No model fine-tuning | LLM not adapted to KG | Fine-tune on KG reasoning |
| Fixed oracle design | Same filtering for all questions | Adaptive filtering by hop depth |

## Recommendations (Future Work)

### Short-term
1. **Replace regex type classifier with LLM-based intent parser**
   - Current: 85% accuracy with 19 regex patterns
   - Goal: Higher recall, fewer false negatives
   
2. **Extend TypeOracle schema beyond 40 Freebase relations**
   - Current: 40 hand-curated relations
   - Goal: Cover more of Freebase's ~24,000 relations

### Medium-term
3. **Explore hybrid oracles (symbolic + embedding)**
   - Combine TypeOracle's precision with embedding's flexibility
   - Recover beam diversity while keeping semantic relevance

4. **Evaluate on CWQ with N ≥ 500**
   - Current: Limited samples
   - Goal: Reduce variance, confirm generalization

### Long-term
5. **Adaptive filtering by hop depth**
   - Looser for 1-hop (less ambiguity)
   - Stricter for 3-hop (more irrelevant paths)

6. **Investigate whether filtering reduces hallucination**
   - Even if Hits@1 drops, does the model hallucinate less?
   - This could be a different optimization target

7. **Cross-domain transfer**
   - Wikidata, ConceptNet, biomedical KGs
   - Test if TypeOracle generalizes beyond Freebase

## The Big Picture

```
Before DCA-Trie:
  "Tighter constraints → better accuracy" (GCR, DoG assumption)

After DCA-Trie:
  "Constraint quality and accuracy are distinct properties"
  "Measure them separately with SIR and Hits@1"
  "Optimize them independently"
```

## If Asked

> **"What are the main conclusions?"**
> "Three things: (1) TypeOracle reduces SIR by 85.5% while maintaining faithfulness. (2) Tighter constraints don't guarantee higher accuracy — the non-monotone result. (3) SIR enables measuring constraint quality independently of answer accuracy."

> **"What are the limitations?"**
> "Freebase-only evaluation, heuristic type inference (85% accuracy), limited schema coverage (40 of 24,000 relations), no fine-tuning, and fixed oracle design."

> **"What should future work focus on?"**
> "Replace regex with LLM-based type extraction, extend schema coverage, explore hybrid oracles, and investigate whether filtering reduces hallucination even if Hits@1 drops."

## Practice
1. Why is the non-monotone finding important for the field?
2. How would you design an adaptive filtering strategy?
3. What would it take to extend TypeOracle to Wikidata?
