# CHAPTER 3

# METHODOLOGY

## 3.1 Introduction

This chapter formalises the permissiveness problem identified in Chapter 2 and presents the Dynamic Context-Aware Trie (DCA-Trie) framework as a solution. The upgraded oracle specification and the Semantic Irrelevance Ratio (SIR) are defined first, with SIR serving as a diagnostic metric that measures constraint quality independently of answer accuracy. The symbolic relevance mechanism shared by both DCA-Trie variants is then described, followed by the static pre-filtering design of v1 and the step-wise dynamic expansion design of v2. The chapter closes with the baseline configurations, evaluation protocol, and scope boundaries that govern the experimental work in Chapter 4.

Unlike earlier embedding-based formulations, the final methodology used in this thesis implements semantic filtering through a deterministic TypeOracle. The TypeOracle uses the knowledge graph's own ontology metadata, especially entity types and relation ranges, instead of sentence-transformer embeddings, cosine similarity, or tuned admission thresholds.

## 3.2 Formal Problem Specification

### 3.2.1 Restating the Core Limitation of Existing Frameworks

As established in Chapter 2, current graph-constrained frameworks, notably Graph-Constrained Reasoning (GCR) (Luo et al., 2025a) and Dynamic-of-Graph (DoG) (Li et al., 2025), rely on a deterministic oracle that looks mainly at the fixed graph G and the starting entities E_q. Regardless of whether the system builds this oracle before decoding or expands it on the fly, the set of valid tokens at any step t remains locked to structural logic:

> W_val^GCR(t) = f(G, E_q), for all t ---(3.1)

Equation (3.1) captures the static constraint model. By ignoring both the semantic intent of the question q and the reasoning trajectory already captured in the prefix y^{<t}, this formulation treats every structurally reachable path as equally plausible. In dense, multi-hop Freebase environments, this blindness causes search space explosion. The framework may admit thousands of paths at deeper hop levels, even though only a small subset can logically answer the query.

The core issue is that these systems conflate two separate requirements. Structural validity ensures the LLM only generates tokens that correspond to real graph edges. Contextual relevance ensures the LLM only generates tokens that logically connect to the specific question at hand. Existing constrained methods are strong at structural compliance but remain permissive with respect to semantic usefulness. This gap between structural compliance and semantic usefulness is the permissiveness problem.

### 3.2.2 The Upgraded Oracle Specification

DCA-Trie addresses this problem by defining an upgraded constraint oracle that combines structural validity with question-aware semantic filtering. The oracle conditions on the knowledge graph, the linked question entities, the input question, and, in the dynamic version, the evolving generation prefix:

> W_val^DCA(t) = f(G, E_q, q, y^{<t}) ---(3.2)

where q is the natural language query and y^{<t} = (y_1, ..., y_{t-1}) is the generated prefix at step t.

To be methodologically sound, the upgraded oracle must satisfy three conditions aligned with the project objectives in Chapter 1:

1. Structural Faithfulness (Condition F): Every candidate token v in W_val^DCA(t) must correspond to a valid prefix of a path in G at every step t. This preserves the structural faithfulness guarantee achieved by graph-constrained decoding and prevents ungrounded tokens from entering the valid set.

2. Semantic Relevance Reduction (Condition R): The Semantic Irrelevance Ratio under DCA-Trie must be lower than the corresponding SIR under GCR when averaged over the evaluation corpus:

> SIR(W^DCA) < SIR(W^GCR) ---(3.3)

3. Recall Preservation (Condition P): Semantic pruning must not remove gold answer paths excessively. Operationally, the false negative rate on the validation set must remain low:

> FNR = |{q in Q_val : p*_q not admitted by W_val^DCA}| / |Q_val| ---(3.4)

where p*_q is the gold path for question q and Q_val is the held-out validation set.

The implemented DCA-Trie oracle satisfies these conditions through conservative symbolic gates. When ontology information is missing, the oracle admits the candidate rather than pruning it. This design reduces semantic irrelevance while avoiding aggressive filtering that could harm answer recall.

## 3.3 System Architecture Overview

DCA-Trie focuses on the constraint oracle layer, so its architecture directly builds on the baseline pipeline from GCR (Luo et al., 2025a). This reuse helps isolate the experimental effects of the proposed oracle. The four layers work as follows:

1. Entity Linking Layer (Unmodified): A named entity recognition or entity-linking component identifies the core query entities E_q from the raw natural language question q. These entities dictate where downstream graph exploration begins.

2. Constraint Oracle Layer (DCA-Trie Contribution): This layer controls which tokens the LLM can generate. In GCR, this layer creates a KG-Trie that includes structurally reachable paths within L hops of the starting entities. DCA-Trie modifies this layer by applying symbolic ontology checks. Through either static pre-filtering (v1) or dynamic step-wise expansion (v2), the oracle ensures that admitted paths remain graph-valid and type-consistent.

3. Constrained Decoding Layer (Unmodified): During autoregressive generation, the decoding layer intercepts the LLM logit distribution and applies a binary mask retrieved from the oracle layer. The LLM is therefore restricted to tokens that are currently valid under the trie.

4. Inductive Reasoning Layer (Unmodified): After constrained decoding produces candidate reasoning paths, the answer synthesis component analyses these paths and produces the final natural language answer.

**Figure 3.1 Placeholder: DCA-Trie System Architecture**

This figure should show the full pipeline: question input, entity linking, KG access, DCA-Trie constraint oracle, constrained beam search, reasoning paths, and final answer synthesis. The oracle box should explicitly show symbolic TypeOracle checks rather than cosine scoring or embedding vectors.

## 3.4 The Semantic Irrelevance Ratio: Definition and Measurement

### 3.4.1 Standard Metric Deficiencies

Current performance markers for knowledge graph decoding, such as Hits@1, F1, and structural faithfulness ratios, have a significant drawback: they focus on output instead of the process. While these metrics show whether a framework found the correct answer and stayed within the graph, they do not reveal how the framework reached that answer. A model may solve the correct gold path, but it could wander through a large number of irrelevant paths that waste resources.

Therefore, confirming accuracy is not enough; the constraint mechanism itself must be measured. To assess how permissive the oracle is, independently of final answer accuracy, this thesis presents a diagnostic metric called the Semantic Irrelevance Ratio (SIR).

### 3.4.2 Formal Definition of SIR

Suppose P(q, t) represents all paths that the constraint oracle allows at decoding step t for question q. To calculate SIR, the system must first define irrelevance. An individual candidate path p in P(q, t) is structurally valid, but it fails the semantic stringency test if its terminal entity type is incompatible with the inferred answer types, or if any edge in the path violates the property range constraint:

> irrelevant(p, q) = 1[not type_gate(p, q) OR EXISTS (e, r, e') in p : not range_gate(r, e')] ---(3.5)

Equation (3.5) defines the binary irrelevance indicator. Here, type_gate checks whether the terminal entity's type matches the expected answer types inferred from the question, and range_gate checks whether each edge respects the ontology's declared property ranges. Both gates are deterministic set operations over the KG's own schema.

The step-level SIR for question q at decoding step t is then defined as:

> SIR(q, t) = SUM over p in P(q,t) of irrelevant(p, q) / |P(q, t)| ---(3.6)

As shown in Equation (3.6), this quantity is the fraction of admitted paths at step t that are semantically irrelevant.

Corpus-level SIR is computed by averaging over all questions and all valid decoding steps up to depth L:

> SIR = (1/|Q|) * SUM over q in Q of (1/L_q) * SUM from t=1 to L_q of SIR(q, t) ---(3.7)

Equation (3.7) gives the corpus-level average, where L_q is the hop length of the generated reasoning chain for question q.

### 3.4.3 Properties and Interpretation

By definition, SIR is in [0, 1]. A value near 1 indicates that most admitted paths are irrelevant, so the model still faces a large and noisy search space. A value near 0 indicates that the constraint set is tightly aligned with question semantics. Prior constrained frameworks such as GCR and DoG tend to show high SIR, especially at larger hop depths where path counts increase rapidly. DCA-Trie is designed to reduce SIR by filtering semantically weak paths while retaining structurally valid ones. In reporting, SIR is analyzed by hop depth to evaluate how this effect scales with reasoning complexity.

## 3.5 Symbolic Relevance Scoring Mechanism

### 3.5.1 TypeOracle Architecture

The symbolic relevance mechanism implements the transition from a static oracle f(G, E_q) to a context-aware oracle f(G, E_q, q, y^{<t}). Unlike embedding-based approaches that compute cosine similarity between dense vectors, the final DCA-Trie implementation uses a TypeOracle: a purely symbolic oracle over the knowledge graph's own ontology schema. All admission decisions are made through set lookups rather than neural encoder forward passes.

The oracle consists of two complementary gates that evaluate candidate paths against KG metadata:

1. Answer Type Gate, rho_e: Applied only at the terminal hop. It checks whether the candidate answer entity's type matches what the question asks for. For example, a question beginning with "who" infers person-type entities as valid answers.

2. Property Range Gate, rho_r: Applied at every hop. It checks whether the tail entity's type is compatible with the relation's declared range in the ontology. For example, if a relation expects a location as its range, then only entities typed as locations are admitted when type information is available.

The combined admission check is:

> is_admissible(r, e', answer_types, hop, max_hop) = type_gate(e', answer_types, hop, max_hop) AND range_gate(r, e') ---(3.8)

A candidate edge consisting of relation r and tail entity e' is admitted if it passes all active gates. This replaces cosine-based relevance scoring entirely. The final method does not use embeddings, forward passes, or threshold tuning for the oracle.

**Figure 3.2 Placeholder: Symbolic Relevance Scoring Mechanism**

This figure should show a candidate relation/entity pair entering the TypeOracle, followed by two checks: property range compatibility and terminal answer-type compatibility. The output should be a binary admit/reject decision.

### 3.5.2 Ontology Schema Construction

The TypeOracle is constructed from the knowledge graph's own schema triples. The Freebase schema available in the WebQSP and CWQ subgraphs encodes ontology information such as:

1. Entity types through `common.topic.notable_types` triples.

2. Property domains through `rdf-schema#domain` triples.

3. Property ranges through `rdf-schema#range` triples.

From these triples, the oracle builds two main lookup structures:

1. `_entity_types`: maps each entity to its set of Freebase types.

2. `_schema`: maps each relation to its domain and range constraints.

Question type inference uses lightweight pattern matching over the natural language question. Typical mappings include:

```text
"who" / "director" / "actor"  ->  person types
"country" / "city" / "where"  ->  location types
"film" / "movie"              ->  creative work types
"when" / "date" / "year"      ->  date types
```

Multiple patterns may match, producing a union of expected answer types. If no pattern matches, the question remains unconstrained at the answer-type level, and the type gate admits candidates conservatively.

### 3.5.3 Threshold-Free Design

The TypeOracle is threshold-free. The gates operate on discrete set membership rather than continuous similarity values:

> type_gate: returns True if types(entity) intersects answer_types.

> range_gate: returns True if types(tail_entity) intersects range(relation).

Both gates are conservative. They return True when the relation is unknown, the entity type is unknown, the relation has no recorded range, or no answer type can be inferred from the question. This conservative design ensures that structural faithfulness is never compromised by the semantic filter and reduces the risk of false negatives caused by incomplete schema metadata.

### 3.5.4 Computational Properties

The symbolic design has different computational properties from the earlier embedding-based formulation:

| Property | Embedding-Based Formulation | Symbolic TypeOracle |
| --- | --- | --- |
| Per-path cost | Encoder forward pass | O(1) set lookup |
| Deterministic | No, due to floating-point similarity | Yes |
| GPU required for oracle | Yes or beneficial | No |
| Admission threshold | Required | Not required |
| Interpretability | Low, based on dense vectors | High, based on type names and ranges |

These properties make the symbolic oracle easier to inspect, cheaper to run, and more closely aligned with the KG schema used for structural grounding.

## 3.6 DCA-Trie v1: Static Symbolic Filtering

### 3.6.1 Design Rationale

DCA-Trie v1 addresses the permissiveness problem while keeping the efficient static-trie design used in GCR. The key idea is to apply symbolic filtering once, before decoding begins, using the KG's ontology schema and the inferred answer type of the question. This is useful because many paths are structurally reachable but type-incompatible with the question's intent. Filtering paths against the ontology during preprocessing removes weak candidates early and reduces the search space before autoregressive generation starts.

**Figure 3.3 Placeholder: Static Symbolic Filtering Pipeline for DCA-Trie v1**

This figure should show BFS path enumeration from question entities, TypeOracle filtering using range_gate and type_gate, construction of a filtered KG-Trie, and constrained decoding from the filtered trie.

### 3.6.2 Algorithm for DCA-Trie v1

**Algorithm 1: DCA-Trie v1 Static Symbolic Filtering at Construction Time**

```text
Require: Knowledge graph G; question entities E_q; question q; max hop depth L; TypeOracle oracle
Ensure: Semantically filtered KG-Trie T_v1

1:  answer_types <- oracle.infer_answer_types(q)
2:  P <- BFS(G, E_q, L)
3:  P_filtered <- empty set
4:  for each path p = (e_0, r_1, e_1, ..., r_L, e_L) in P do
5:      admit <- True
6:      for each hop (r_i, e_i) in p do
7:          if NOT oracle.range_gate(r_i, e_i) then
8:              admit <- False
9:              break
10:         end if
11:     end for
12:     if admit AND NOT oracle.type_gate(e_L, answer_types, L, L) then
13:         admit <- False
14:     end if
15:     if admit then
16:         P_filtered <- P_filtered UNION {p}
17:     end if
18: end for
19: T_v1 <- BuildTrie(P_filtered)
20: return T_v1
```

The process unfolds in five stages:

1. Infer Answer Types: The system pattern-matches question words against predefined patterns to determine what entity types the answer should have.

2. Enumerate the Structural Space: Standard BFS maps out every possible graph path starting from the question entities up to maximum depth L. This matches the baseline GCR approach.

3. Apply Symbolic Filtering: For each enumerated path, the oracle checks whether every edge respects the relation's declared range and whether the terminal entity type matches the inferred answer types.

4. Construct the Static Trie: The remaining paths are compiled into a static prefix tree T_v1.

5. Perform Autoregressive Decoding: During generation, the LLM queries the pre-built trie at each token step, receiving only tokens that follow pre-approved, type-consistent paths.

### 3.6.3 Complexity Analysis

Building T_v1 has an offline cost of O(|P| * L), where |P| is the number of BFS-enumerated paths and L is the maximum hop depth. Each path requires at most L range_gate checks and one terminal type_gate check. Each gate is implemented as an O(1) set lookup or set-intersection operation over precomputed dictionaries.

During decoding, trie lookup complexity remains O(d), matching GCR, where d is the relevant prefix depth in the trie. Memory usage scales as O(|P_filtered| * L), typically smaller than GCR's O(|P| * L), because symbolic filtering removes type-incompatible paths before trie construction.

### 3.6.4 Faithfulness Guarantee

DCA-Trie v1 maintains structural faithfulness by design. Every path kept in P_filtered comes from BFS(G, E_q, L), ensuring that each triplet (e_{i-1}, r_i, e_i) remains a valid graph edge. Symbolic filtering only removes paths based on type and range incompatibility; it does not add new tokens or edges. Therefore, any token passed through T_v1 remains structurally grounded, satisfying Condition F.

## 3.7 DCA-Trie v2: Step-Wise Symbolic Expansion

### 3.7.1 Design Rationale

DCA-Trie v2 implements the dynamic oracle by conditioning constraints on the evolving prefix y^{<t}. Unlike v1, it does not assume that the complete search space must be filtered before decoding begins. As generation progresses, y^{<t} reveals the path decisions already made, so the relevant neighbourhood can change step by step.

Architecturally, v2 follows the step-wise traversal pattern in DoG (Li et al., 2025) but adds symbolic gating to each local expansion. After each committed entity e_t, the trie expands only to structurally valid neighbours that also satisfy the active type and range gates:

> T_{t+1} = T_t UNION {(e_t, r, e') : (e_t, r, e') in G AND type_gate(e', answer_types, hop, L) AND range_gate(r, e')} ---(3.9)

The core difference from permissive dynamic expansion is therefore not when expansion happens, but how candidates are admitted. Every step remains graph-valid and type-consistent.

**Figure 3.4 Placeholder: Step-Wise Symbolic Expansion Workflow for DCA-Trie v2**

This figure should show the current trie, token lookup, masked LLM decoding, entity commitment, local neighbour expansion from the KG, TypeOracle checks, and trie update.

### 3.7.2 Algorithm for DCA-Trie v2

**Algorithm 2: DCA-Trie v2 Step-Wise Symbolic Expansion**

```text
Require: Knowledge graph G; question entities E_q; question q; TypeOracle oracle; LLM with vocabulary V
Ensure: Generated reasoning chain y_1 ... y_T

1:  T_0 <- {e_q : e_q in E_q}
2:  answer_types <- oracle.infer_answer_types(q)
3:  for each step t = 1 to T do
4:      V_t <- TrieLookup(T_{t-1}, y^{<t})
5:      m_t[v] <- 1[v in V_t] for all v in V
6:      alpha_t <- m_t * LLMLogits(y^{<t}, x)
7:      y_t <- beam_search_step(alpha_t)
8:      if y_t is an entity token e_t then
9:          for each (e_t, r, e') in G do
10:             if oracle.range_gate(r, e') then
11:                 if oracle.type_gate(e', answer_types, hop, L) then
12:                     Add (e_t, r, e') to T_t
13:                 end if
14:             end if
15:         end for
16:     else
17:         T_t <- T_{t-1}
18:     end if
19: end for
20: return y_1 ... y_T
```

Unlike the static approach in v1, Algorithm 2 combines generation and symbolic filtering:

1. Initialize a Minimal State: The system starts with a basic trie containing only the root question entities and the inferred answer types.

2. Generate under Current Constraints: At each step t, the LLM produces a token strictly limited by the current trie boundaries.

3. Check for Entity Commitment: If the LLM generates an entity token, it triggers an expansion phase. Relation tokens do not trigger expansion.

4. Apply Symbolic Expansion: When an entity is committed, the system examines all structurally valid neighbours from the master KG. Each candidate is checked by range_gate and, where applicable, type_gate. Only candidates passing the active gates are added to the trie.

This yields an adaptable oracle that builds the search space one step ahead of the model's reasoning state using deterministic set operations.

## 3.8 Baseline Systems

Four system configurations are evaluated to assess the proposed methodology:

1. CoT Baseline: The same Llama-3.1-8B model (Dubey et al., 2024) used in the GCR setting, run without any KG constraint oracle and prompted with standard chain-of-thought reasoning. This provides the unconstrained reference point.

2. GCR: The original Graph-Constrained Reasoning framework (Luo et al., 2025a) with static KG-Trie constraints W_val(t) = f(G, E_q). This is the primary constrained baseline.

3. DCA-Trie v1: The static symbolic filtering variant described in Section 3.6, implemented as a preprocessing step in the GCR pipeline. It constructs a filtered trie using TypeOracle range and answer-type checks.

4. DCA-Trie v2: The dynamic step-wise expansion variant described in Section 3.7, integrated into the decoding process. It expands the trie after entity commitments and applies TypeOracle checks to each newly discovered candidate.

To ensure fair comparison, all settings use the same backbone model, the same entity-linking pipeline for E_q, and matched decoding settings for constrained systems. This isolates differences to the constraint-oracle design rather than model or preprocessing variation.

## 3.9 Evaluation Protocol

### 3.9.1 Datasets

Evaluation is conducted on two standard Freebase-based KGQA datasets (Bollacker et al., 2008):

1. WebQSP (Yih et al., 2016): A benchmark of natural language questions over Freebase, mostly requiring one-hop and two-hop reasoning. The standard test set is used for evaluation, with a held-out validation subset used for development checks.

2. ComplexWebQuestions (CWQ) (Talmor and Berant, 2018): A larger KGQA benchmark with higher compositional complexity and hop depths up to four. This dataset tests whether the method remains effective when reasoning paths become deeper and more branching.

### 3.9.2 Evaluation Metrics

Five metrics are used across both datasets:

1. Hits@1: The proportion of examples where the top predicted answer matches the gold entity.

2. F1: Entity-level overlap score for settings with multiple acceptable answers, following common KGQA evaluation practice.

3. Structural Faithfulness Rate: The fraction of generated paths where all triplets are valid in the underlying KG.

4. Semantic Irrelevance Ratio (SIR): Computed using the symbolic type and range definitions in Equations (3.5), (3.6), and (3.7). This measures the proportion of admitted paths that remain semantically weak despite being structurally valid.

5. Average Trie Size Per Step: The mean size of the valid token set |V_t| across decoding steps, used as a direct efficiency indicator of constraint selectivity.

### 3.9.3 Hop-Depth Stratification

All major metrics are also reported by hop depth, such as one-hop, two-hop, three-hop, and four-hop questions, consistent with prior KGQA analysis. This is important because permissiveness effects usually increase with hop depth. Reporting only aggregate results can hide this behaviour.

### 3.9.4 Experimental Configuration

The constrained systems use the same LLM backbone and comparable decoding settings so that performance differences can be attributed to the oracle design. The TypeOracle itself is lightweight and does not require GPU acceleration because its decisions are based on dictionary lookups and set intersections over precomputed schema metadata.

For the constrained systems, beam search is used with a matched beam width. Maximum generation length is set according to the maximum hop depth of the dataset, with shorter limits for WebQSP and longer limits for CWQ. Since the final oracle does not use a sentence encoder, no sentence-transformer model or embedding cache is required for DCA-Trie filtering.

## 3.10 Scope Boundaries and Anticipated Limitations

This study has clear scope boundaries that frame the interpretation of the Chapter 4 results:

1. Single KG and Domain: Experiments are limited to Freebase-based KGQA. Generalization to other KGs, such as Wikidata and ConceptNet, remains future work.

2. No Model Fine-Tuning: The LLM backbone is not fine-tuned. Observed improvements reflect changes in constraint-oracle design rather than adaptation of model parameters.

3. Empirical Faithfulness Evidence: Condition F is assessed empirically by checking generated paths against KG triplets, following established practice in prior work. This evidence is interpreted under the same implementation assumptions regarding valid-token masking and tokenizer alignment.

4. Schema Coverage Dependence: The TypeOracle depends on the availability and quality of entity type and relation range metadata. Missing or incomplete schema information can reduce the oracle's ability to filter irrelevant paths.

5. Conservative Admission Policy: To preserve recall, the oracle admits candidates when ontology information is missing. This reduces false negatives but means that some irrelevant paths may still pass through the trie.

6. Heuristic Question Type Inference: The current answer-type inference uses lightweight pattern matching over question words. This is transparent and efficient, but it may miss complex linguistic cues that require deeper semantic parsing.

7. Runtime Overhead from Graph Traversal: Although TypeOracle checks are cheap, DCA-Trie still depends on graph traversal and trie construction or expansion. Wall-clock latency is therefore affected by graph density, hop depth, and implementation choices.

Together, these boundaries clarify that the contribution of this thesis is not a new language model or a fine-tuning method, but a symbolic constraint-oracle design that makes graph-constrained decoding less permissive while preserving structural grounding.
