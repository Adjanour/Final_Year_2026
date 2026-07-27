# Guide 6: TypeOracle — The Two Gates

## What This Section Covers
The TypeOracle design, the two gates, and how they work together.

## The TypeOracle

A purely symbolic type oracle using the Freebase ontology schema. No embeddings, no threshold, O(1) per candidate.

### What It Uses from Freebase
- **Entity types**: via `common.topic.notable_types`
  - Example: Paris → {City, Place}
  - Example: France → {Country}
- **Relation ranges**: via `rdf-schema#range`
  - Example: capital_of → {Country}
  - Example: spouse_of → {Person}

## Gate 1: Range Gate (every hop)

**Question**: Does the tail entity's type match the relation's range?

$$\text{range\_gate}(r, e') = \mathbb{1}\bigl[\text{types}(e') \cap \text{range}(r) \neq \emptyset\bigr]$$

**In plain English**: If the relation is "capital_of" (which requires a Country), is the candidate entity actually a Country?

**Example**:
- Relation: capital_of, Range: {Country}
- Candidate: France → types: {Country} → Country ∈ {Country} → ✅ PASS
- Candidate: Paris → types: {City, Place} → City ∉ {Country} → ❌ FAIL

**Applied at**: Every hop (1st, 2nd, 3rd, etc.)

## Gate 2: Type Gate (terminal hop only)

**Question**: Does the terminal entity's type match the inferred answer type?

$$\text{type\_gate}(e', q, h, L) = \mathbb{1}\bigl[\text{types}(e') \cap \mathcal{T}(q) \neq \emptyset\bigr]$$

**In plain English**: If the question asks "who", is the candidate a Person? If it asks "where", is it a Location?

**Example**:
- Question: "Who is the spouse of the ex-president of USA?"
- Inferred answer type: {Person}
- Terminal entity: Laura Bush → types: {Person} → Person ∈ {Person} → ✅ PASS
- Terminal entity: Washington D.C. → types: {City} → City ∉ {Person} → ❌ FAIL

**Applied at**: Only the terminal hop (the last hop in the path)

## How They Work Together

```
For each candidate path: head → relation → tail

Step 1: Range gate (every hop)
  - Does tail type match relation range?
  - If NO → reject path
  - If YES → continue

Step 2: Type gate (terminal hop only)
  - Is this the last hop?
  - If YES: Does tail type match answer type?
    - If NO → reject path
    - If YES → accept path
  - If NO: continue to next hop
```

## Type Inference

How do we know what type the answer should be?

- **Regex classifier**: 19 patterns that map question words to Freebase types
  - "who" → Person
  - "where" → Location
  - "when" → Date/Time
  - "what organization" → Organization
- **Fallback**: If no pattern matches, conservatively admit all candidates

## Unknown Schema Handling

If the TypeOracle doesn't have schema information for a relation or entity:
- **Conservative approach**: Admit the candidate (don't reject what you don't know)
- This ensures FNR stays below 5%

## If Asked

> **"What are the two gates?"**
> "Range gate checks if the tail entity's type matches the relation's range — applied at every hop. Type gate checks if the terminal entity matches the inferred answer type — applied only at the last hop."

> **"Why no embeddings?"**
> "Embeddings require a threshold τ that's sensitive to the dataset. Symbolic gates are deterministic, O(1), and don't need tuning. Same input always gives same output."

> **"What happens if the oracle doesn't know a type?"**
> "It conservatively admits the candidate. This ensures we don't accidentally remove correct paths (FNR < 5%)."

## Practice
1. Why is the range gate applied at every hop but the type gate only at the terminal hop?
2. What would happen if we applied the type gate at every hop?
3. How does the regex classifier handle "what is the capital of France?" vs "who invented the telephone?"
