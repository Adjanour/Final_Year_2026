# Guide 7: SIR — The New Metric

## What This Section Covers
The Semantic Irrelevance Ratio (SIR) — what it measures, how to compute it, and why it matters.

## What is SIR?

**SIR** measures the fraction of candidate paths that are *semantically irrelevant* to the question — paths that exist in the KG but don't actually help answer the question.

$$\text{SIR}(q, t) = \frac{\sum_{p \in \mathcal{P}(q, t)} \text{irrelevant}(p, q)}{|\mathcal{P}(q, t)|}$$

**In plain English**: Out of all paths available at hop $t$, what fraction are useless?

## Corpus Average SIR

$$\overline{\text{SIR}} = \frac{1}{|Q|} \sum_{q \in Q} \frac{1}{L_q} \sum_{t=1}^{L_q} \text{SIR}(q, t)$$

- Average over all questions
- Average over all hops per question
- Range: 0 (perfect — no irrelevant paths) to 1 (worst — all paths irrelevant)

## Example Calculation

**Question**: "Who is the spouse of the ex-president of USA?"

**Hop 1** (from USA):
- Available paths: USA → ex-president → {GWB, BO, DT}
- Relevant paths: USA → ex-president → {GWB, BO} (both are ex-presidents)
- Irrelevant paths: USA → ex-president → {DT} (DT is not ex-president at time of data)
- SIR at hop 1 = 1/3 = 0.33

**Hop 2** (from GWB/BO/DT):
- Available paths: {GWB → spouse → LB, BO → spouse → MO, DT → spouse → MT}
- All are valid spouse relations
- SIR at hop 2 = 0/3 = 0.0

**Question SIR** = (0.33 + 0.0) / 2 = 0.165

## Why SIR Matters

| Method | SIR | Interpretation |
|--------|-----|----------------|
| GCR Baseline | 1.0 | All paths admitted (no filtering) |
| DCA-Trie v1 | 0.145 | 85.5% of irrelevant paths removed |

**Before SIR**: You could only measure accuracy (Hits@1). If accuracy dropped, you didn't know if it was because:
- The constraint removed correct paths (bad), or
- The constraint removed irrelevant paths but the LLM couldn't find the answer anyway (neutral)

**With SIR**: You can separately measure constraint quality (SIR) and answer quality (Hits@1).

## SIR vs Accuracy: The Non-Monotone Result

| Metric | GCR | DCA-Trie v1 | Change |
|--------|-----|-------------|--------|
| SIR | 1.000 | 0.145 | -85.5% (better) |
| Hits@1 | 91.6% | 86.4% | -5.2pp (worse) |

**Key finding**: Tighter constraints (lower SIR) do NOT guarantee higher accuracy. This is the non-monotone result.

## If Asked

> **"What is SIR?"**
> "Semantic Irrelevance Ratio — the fraction of structurally valid paths that are semantically irrelevant to the question. Lower is better. GCR has SIR = 1.0 (all paths admitted), DCA-Trie v1 has SIR = 0.145 (85.5% of irrelevant paths removed)."

> **"Why is SIR important?"**
> "It's the first metric that measures constraint quality independently of answer accuracy. Before SIR, you couldn't tell if a tighter constraint was actually filtering relevant paths or just removing everything."

> **"What did you find?"**
> "TypeOracle reduced SIR by 85.5%, but Hits@1 dropped by 5.2pp. This shows constraint tightness and answer accuracy are not monotonically related."

## Practice
1. Calculate SIR for a question with 10 paths at hop 1, where 3 are irrelevant, and 5 paths at hop 2, where 1 is irrelevant.
2. Why do we average over hops, not just take the final hop's SIR?
3. What would SIR = 0 mean? Is that achievable?
