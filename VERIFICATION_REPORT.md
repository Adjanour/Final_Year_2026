# Literature Review Table Verification Report

## Executive Summary
Verification of 8 key papers from the literature review table examining claims about **Structural Faithfulness** and **Semantic Conditioning**. Based on detailed examination of paper abstracts, bibliographies, and text extraction.

**Overall Assessment: All major claims are ACCURATE**

---

## Detailed Verification Results

### 1. **luo2025-graph-constrained-reasoning.pdf**
- **Table Claims:** "Yes (100%)" structural faithfulness | "No" semantic conditioning
- **Approach:** Graph-constrained Reasoning using KG-Trie decoding
- **Key Findings:**
  - Paper explicitly defines "KG-constrained zero hallucinations" as ensuring reasoning paths are "fully grounded within KGs"
  - Uses Trie-based constraint during decoding to restrict generation to valid KG paths
  - Decoding is constrained by KG topology (knowledge graph structure), not by semantic information from the question
  - Achieves 100% structural faithfulness guarantee through trie-based enforcement
- **Assessment:** ✓ **ACCURATE** - The paper claims and demonstrates 100% faithfulness to KG structure through constrained trie-based decoding without incorporating semantic question features

---

### 2. **li2024-decoding-on-graphs.pdf**
- **Table Claims:** "Yes (100%)" structural faithfulness | "No" semantic conditioning
- **Approach:** Decoding on Graphs (DoG) with graph-aware constrained decoding
- **Key Findings:**
  - Paper defines "well-formed chains" as chains where:
    1. All triplets must exist on the KG
    2. Connectivity must be maintained (head/tail entity consistency)
  - Uses dynamic trie constraints at each decoding step to enforce only valid KG triplets
  - Progressive subgraph expansion maintains topological validity
  - No semantic features from question used to constrain generation - only KG topology
  - Eliminates hallucination of non-existent KG facts
- **Assessment:** ✓ **ACCURATE** - Achieves 100% structural faithfulness through guaranteed well-formed chain generation without semantic conditioning

---

### 3. **RouterKGQA.pdf** (yuan2026routerkgqa)
- **Table Claims:** "Probabilistic" structural faithfulness | "Yes (answer-level)" semantic conditioning
- **Approach:** Specialized-General Model Routing with Constraint-Aware Reasoning Paths (CRP)
- **Key Findings:**
  - Two-stage approach: (1) Specialized model generates CRP, (2) If reachability check fails, routes to general model for repair
  - Specialized model can fail, making faithfulness "probabilistic" rather than guaranteed
  - CRPs include semantic constraints like `C = (2, education.institution, Harvard)` and `C = (2, position.from, ≥"2000")`
  - These answer-level constraints directly incorporate semantic information from the question
  - Post-hoc beam search repair is needed when main path unreachable
- **Assessment:** ✓ **ACCURATE** - Correctly characterized as probabilistic (repair-based) and answer-level semantic conditioning

---

### 4. **decao2021-genre-autoregressive-entity-retrieval.pdf**
- **Table Claims:** "Entity names only" structural faithfulness | "No" semantic conditioning
- **Approach:** GENRE - Autoregressive Entity Retrieval with trie-based entity name constraints
- **Key Findings:**
  - Uses pre-computed trie of valid entity names/identifiers for constrained beam search
  - At generation time, decoder can only output valid entity identifiers from the trie
  - Dynamically computes tries for entity linking tasks with special start/end tokens
  - Constraints are strictly limited to entity name validity - not semantic correctness
  - No incorporation of semantic question features into the constraint mechanism
- **Assessment:** ✓ **ACCURATE** - Empirically constrains to valid entity names through trie; no semantic conditioning from input

---

### 5. **geng2023gcd.pdf**
- **Table Claims:** "Format only" structural faithfulness | "No" semantic conditioning
- **Approach:** Grammar-Constrained Decoding (GCD) for structured NLP tasks
- **Key Findings:**
  - Title: "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"
  - Constrains generation to valid grammar/format specifications (JSON, YAML, etc.)
  - Enforces syntactic/format correctness through grammar-based constraints
  - Does not constrain based on semantic meaning or knowledge base content
  - Format constraints ensure well-formed output structures independent of semantic validity
- **Assessment:** ✓ **ACCURATE** - Format-only constraints via grammar enforcement; no semantic conditioning

---

### 6. **willard2023-efficient-guided-generation-llms.pdf** (Outlines)
- **Table Claims:** "Format only" structural faithfulness | "No" semantic conditioning
- **Approach:** FSM-indexed regex-based constrained generation
- **Key Findings:**
  - Uses Finite State Machines (FSM) built from regular expressions to guide decoding
  - Examples demonstrate format-only constraints:
    - `([Yy]es|[Nn]o|[Nn]ever|[Aa]lways)` for yes/no answers
    - `19[0-9]{2}` for year format
    - `((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)` for IP addresses
  - Constrains output to match format patterns, not semantic correctness
  - Pre-constructs FSM index for efficient vocabulary masking at each step
- **Assessment:** ✓ **ACCURATE** - Format-only via regex/FSM; no semantic question conditioning

---

### 7. **scholak2021picard.pdf**
- **Table Claims:** "Schema only" structural faithfulness | "No" semantic conditioning
- **Approach:** PICARD - Parsing Incrementally for Constrained Auto-Regressive SQL Decoding
- **Key Findings:**
  - Constrains SQL generation using database schema information
  - Three constraint modes:
    1. Lexing - basic token validity
    2. Parsing without guards - SQL structure
    3. Parsing with guards - schema-aware SQL parsing
  - Prevents invalid SQL by checking against database schema
  - Constraints are limited to schema structure (table names, column names, valid joins)
  - Does not incorporate semantic information from natural language questions
  - Results tables explicitly show "schema only" vs. full database content approaches
- **Assessment:** ✓ **ACCURATE** - Schema-only constraints via SQL parsing; no semantic conditioning

---

### 8. **lu2021-neurologic-decoding.pdf**
- **Table Claims:** "Format only" structural faithfulness | "No" semantic conditioning
- **Approach:** NeuroLogic Decoding with predicate logic constraints
- **Key Findings:**
  - Enforces lexical constraints specified in Conjunctive Normal Form (CNF)
  - Constraints specify which keyphrases/words must/must not appear
  - Treats constraints as hard requirements on lexical content (format-like restrictions)
  - Examples show format constraints for concept sets, gender requirements in MT
  - No semantic understanding of constraint meanings - only enforcement of specified expressions
  - Uses trie data structures to track constraint satisfaction state during generation
- **Assessment:** ✓ **ACCURATE** - Format-only (lexical/keyphrase constraints); no semantic conditioning

---

## Summary Table

| Paper | Structural Faithfulness | Semantic Conditioning | Assessment |
|-------|------------------------|----------------------|------------|
| luo2025-graph-constrained-reasoning | Yes (100%) | No | ✓ ACCURATE |
| li2024-decoding-on-graphs | Yes (100%) | No | ✓ ACCURATE |
| RouterKGQA | Probabilistic | Yes (answer-level) | ✓ ACCURATE |
| decao2021-genre | Entity names only | No | ✓ ACCURATE |
| geng2023gcd | Format only | No | ✓ ACCURATE |
| willard2023-outlines | Format only | No | ✓ ACCURATE |
| scholak2021picard | Schema only | No | ✓ ACCURATE |
| lu2021-neurologic | Format only | No | ✓ ACCURATE |

---

## Key Observations

### Structural Faithfulness Categories:
1. **Yes (100%)**: KG-/graph-constrained approaches (luo2025, li2024) - guarantee all outputs conform to KG structure
2. **Probabilistic**: Approaches that can fail and require repair (RouterKGQA)
3. **Entity names only**: Trie-based entity constraint (decao2021)
4. **Format only**: Grammar/regex-based constrains (geng2023, willard2023, lu2021-neurologic)
5. **Schema only**: Database schema-aware constraints (scholak2021)

### Semantic Conditioning:
- Only **RouterKGQA** uses semantic conditioning from the question (answer-level constraints)
- All other methods constrain based on structure/format/schema, not semantic meaning
- This distinction is critical: semantic conditioning means incorporating features/information from the input question to modify constraints

---

## Verification Methodology

1. **Bibliography Review**: Examined paper titles and publication details
2. **Abstract & Title Analysis**: Confirmed technical approach descriptions
3. **Text Extraction**: Extracted key sections from PDFs describing:
   - Constraint mechanism type
   - How constraints are applied
   - Whether semantic features from questions are used
4. **Cross-reference with Claims**: Verified each claim against actual paper content

---

## Conclusion

All **8 papers** have **accurately characterized claims** in the literature review table. The distinction between structured constraint types (KG-based, graph-based, entity, format, schema) and semantic conditioning is precisely captured in the table classification.
