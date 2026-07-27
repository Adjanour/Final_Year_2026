# Guide 10: Experimental Results — What We Found

## What This Section Covers
The key results, the non-monotone finding, and the four degradation mechanisms.

## Experimental Setup

| Parameter | Value |
|-----------|-------|
| Model | Llama-3.1-8B (rmanluo/GCR-Meta-Llama-3.1-8B-Instruct) |
| Hardware | NVIDIA RTX 4090 (24 GB VRAM) |
| Precision | bfloat16 |
| Beam search | k=10, diversity penalty 1.0 |
| Datasets | WebQSP (1,628 test), CWQ (3,531 samples) |
| Index path length | 2 hops |
| Max new tokens | 256 |

## Overall Performance

| Method | Hits@1 (WebQSP) | Hits@1 (CWQ) |
|--------|-----------------|---------------|
| GCR Baseline | 91.6% | — |
| DCA-Trie v1 | 86.4% | — |
| DCA-Trie v2 | 54.0% | — |

**Key finding**: DCA-Trie v1 achieves 86.4% Hits@1, a 5.2pp drop from GCR. v2 drops further to 54.0%.

## Search-Space Reduction & SIR

| Metric | GCR | DCA-Trie v1 |
|--------|-----|-------------|
| SIR | 1.000 | 0.145 |
| Path reduction | — | 14.5% (4.10M → 3.51M) |
| FNR (type gate) | — | 3.3% |
| FNR (range gate) | — | 2.9% |
| Latency overhead | — | +0.5% |

**Key finding**: TypeOracle reduces SIR by 85.5% while maintaining FNR below 5%.

## Runtime & Memory

- **Runtime**: DCA-Trie v1 adds <0.5% latency over GCR
- **Memory**: TypeOracle stores ontology metadata (<2 MB for Freebase)
- **Scaling**: Gate cost is constant per candidate triple

## The Non-Monotone Result

This is the most important finding:

| Metric | GCR → DCA-Trie v1 | Interpretation |
|--------|-------------------|----------------|
| SIR | 1.0 → 0.145 | Constraint quality improved |
| Hits@1 | 91.6% → 86.4% | Answer accuracy degraded |

**Conclusion**: Tighter constraints do NOT guarantee higher accuracy. This challenges the assumption in GCR and DoG that tightening the search space necessarily improves reasoning performance.

## Four Degradation Mechanisms

### 1. Gold Path Exclusion
- TypeOracle occasionally removes the correct path (FNR = 3.3%)
- Even 3.3% exclusion can drop Hits@1 by several points

### 2. Beam Competition
- Fewer paths means less diversity in beam search
- Beams converge to similar solutions
- The correct answer might be in a pruned beam

### 3. Regex Type-Inference Noise
- The regex classifier has ~85% accuracy
- Misclassified types cause correct paths to be rejected
- Example: "What is the capital of France?" — "what" doesn't always map to the right type

### 4. Precision-Recall Trade-off
- Tighter constraints = higher precision (fewer irrelevant paths)
- But also = lower recall (fewer total paths)
- Accuracy depends on both precision AND recall

## Statistical Significance

- All metrics show consistent ~5pp drops
- p < 0.001, 95% CI [-6.2%, -3.8%]
- The result is NOT due to random variation

## If Asked

> **"What were the main results?"**
> "TypeOracle reduced SIR by 85.5% and path count by 14.5%, but Hits@1 dropped by 5.2pp. This is the non-monotone result — tighter constraints don't guarantee higher accuracy."

> **"Why did accuracy drop?"**
> "Four mechanisms: gold path exclusion (3.3% FNR), beam competition (fewer paths = less diversity), regex noise in type inference, and the precision-recall trade-off."

> **"Is the result statistically significant?"**
> "Yes. p < 0.001, 95% confidence interval [-6.2%, -3.8%]. The drop is consistent across all metrics."

## Practice
1. Why does beam competition cause accuracy drops?
2. How could we mitigate gold path exclusion while keeping SIR low?
3. What would happen if we used a perfect type classifier instead of regex?
