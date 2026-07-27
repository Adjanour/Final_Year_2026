# Guide 2: Problem Statement — Why GCR Is Not Enough

## What This Section Covers
The three specific problems with GCR that DCA-Trie addresses.

## The Three Problems

### Problem 1: Static Trie
- GCR builds the KG-Trie BEFORE decoding starts
- The trie never changes — it's the same at step 1 and step 10
- But the question intent becomes clearer as the model generates more tokens
- **Analogy**: Like looking at a full restaurant menu when you've already decided to order pasta

### Problem 2: No Question Conditioning
- GCR's valid tokens depend on $G$ (graph) and $E_q$ (entities), but NOT on $q$ (the question)
- Two different questions about the same entities get the SAME trie
- "Who is the spouse of Obama?" and "What did Obama do?" get identical constraint sets
- **The LLM must do the semantic filtering itself** — which is exactly what causes hallucination

### Problem 3: No Metric for Constraint Quality
- Existing work assumes "tighter constraints → better accuracy"
- But no metric exists to MEASURE constraint quality independently of answer quality
- You can't optimize what you can't measure

## Formal Statement

**Core limitation of existing frameworks:**
$$\mathcal{W}_{\text{val}}^{\text{GCR}}(t) = f(\mathcal{G}, \mathcal{E}_q) \quad \forall t$$

The valid token set is IDENTICAL at every decoding step $t$.

**DCA-Trie extends this to:**
$$\mathcal{W}_{\text{val}}^{\text{DCA}}(t) = f(\mathcal{G}, \mathcal{E}_q, q, y_{<t})$$

Now it also depends on the question $q$ and partial output $y_{<t}$.

## Design Conditions

| Condition | What it means | How to verify |
|-----------|--------------|---------------|
| **F** (Faithfulness) | 100% structural grounding in KG triplets | Check every generated triple exists in the KG |
| **R** (Relevance) | Lower SIR than baseline | Measure SIR before and after TypeOracle |
| **P** (Recall) | FNR on gold paths < 5% | Check if TypeOracle accidentally removes correct paths |

## If Asked

> **"What is the permissiveness problem?"**
> "GCR admits all structurally valid paths, but most are semantically irrelevant. A 3-hop question can have 24,000 valid paths, only 1 correct. The LLM must filter the rest using the same internal knowledge that causes hallucination."

> **"Why is the static trie a problem?"**
> "The trie is fixed before decoding starts. It can't adapt to the question intent or the evolving reasoning chain. Two different questions about the same entities get the same constraint set."

## Practice
1. Why can't we just make the trie tighter to improve accuracy? (Hint: think about the non-monotone result)
2. What would happen if we conditioned the trie on the full question but not the partial output?
3. Why is FNR < 5% an important design constraint?
