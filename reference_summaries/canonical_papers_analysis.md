# Canonical Papers Analysis — Sentence Patterns, Grammar, and Wording

Three papers selected as writing models for the DCA-Trie journal paper. Each analyzed for: (1) what the paper actually says in human terms, (2) sentence-level patterns, (3) grammar structures, (4) specific wording choices to borrow.

---

## Paper 1: GCR — Luo et al. (2025)

**Full title:** Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models
**Venue:** ICML 2025
**File:** papers/Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models.pdf

### Human-Term Summary

LLMs are good at reasoning but make things up. Knowledge graphs (KGs) have real facts stored as triples. The problem is: how do you force an LLM to only generate reasoning paths that actually exist on the KG?

Previous work either (a) retrieves facts and feeds them to the LLM as input (retrieval-based), or (b) lets the LLM act as an agent that pokes at the KG step by step (agent-based). Both have problems: retrieval needs a good retriever, agent-based is slow and expensive.

GCR's insight: convert the KG into a trie (prefix tree), then use that trie to constrain what tokens the LLM can generate during decoding. The LLM literally cannot hallucinate a path that doesn't exist on the KG because the trie blocks invalid tokens. They use a small fine-tuned LLM for the constrained generation, then a big general LLM (ChatGPT) to reason over the multiple paths and pick the answer.

Result: zero hallucination in reasoning paths, state-of-the-art accuracy, and it generalizes to new KGs without retraining.

### Sentence Patterns

**Opening the problem (Introduction):**
```
Large language models (LLMs) have shown impressive reasoning abilities in handling
complex tasks [cite], marking a significant leap that bridges the gap between human
and machine intelligence. However, LLMs still struggle with conducting faithful
reasoning due to issues of lack of knowledge and hallucination [cite].
```
Pattern: `[Positive claim with citation]. However, [negative claim with citation].`

**Categorizing existing work:**
```
Existing KG-enhanced LLM reasoning methods can be roughly categorized into two
groups: retrieval-based and agent-based paradigms, as shown in Figure 2 (a) and (b).
```
Pattern: `Existing [X] methods can be roughly categorized into [N] groups: [A] and [B].`

**Introducing the method:**
```
To this end, we introduce graph-constrained reasoning (GCR), a novel KG-guided
reasoning paradigm that connects unstructured reasoning in LLMs with structured
knowledge in KGs, seeking to eliminate hallucinations during reasoning on KGs and
ensure faithful reasoning.
```
Pattern: `To this end, we introduce [NAME], a novel [TYPE] that [WHAT IT DOES], seeking to [GOAL].`

**Explaining the mechanism:**
```
Inspired by the concept that LLMs reason through decoding [cite], we incorporate
the KG structure into the LLM decoding process. This enables LLMs to directly
reason on graphs by generating reliable reasoning paths grounded in KGs that lead
to correct answers.
```
Pattern: `Inspired by [INSIGHT], we [ACTION]. This enables [CAPABILITY].`

**Results as tension:**
```
Among the LLM reasoning methods, ChatGPT with self-consistency prompts demonstrates
the best performance, which indicates the powerful reasoning ability inherent in LLMs.
However, their performances are still limited by the model size and complex reasoning
required over structured data.
```
Pattern: `[Method X] demonstrates [positive result], which indicates [positive claim]. However, [remaining limitation].`

**Limitations section:**
```
This shows that KG constraints not only improve reasoning by reducing the searching
space, but also play a crucial role in preventing hallucinations for accurate reasoning.
```
Pattern: `This shows that [X] not only [first benefit], but also [second benefit].`

### Grammar Structures

1. **Passive voice for established facts, active for contributions:**
   - Passive: "Knowledge graphs (KGs) have been utilized to enhance LLM reasoning"
   - Active: "we introduce graph-constrained reasoning (GCR)"
   - Active: "we propose a KG-Trie to encode paths"

2. **Conditional framing for design choices:**
   - "Given a KG G and a question q, we first retrieve paths..."
   - "After a valid reasoning path is generated, we switch back to the regular decoding process"

3. **Hedging with "can" and "may" for limitations:**
   - "which may not generalize well to unseen questions"
   - "the trained retriever may struggle with out-of-domain scenarios"

4. **Equation introduction pattern:**
   - "formulated as:" then equation
   - "where [variables] denote [meanings]"

### Wording Choices to Borrow

| Their phrasing | When to use it |
|---|---|
| "To this end" | When transitioning from problem to method (replaces "Therefore") |
| "Inspired by the concept that" | When grounding your design in someone else's insight |
| "This enables LLMs to directly" | When explaining what your method makes possible |
| "resulting in" | When describing downstream effects |
| "faithful reasoning" | When arguing your method prevents hallucination |
| "grounded in KGs" | When emphasizing KG-constrained output |
| "In this way, [X] combines" | When summarizing how two components work together |
| "the main contributions of this work are as follows:" | Standard contribution list intro |
| "Extensive experiments demonstrate that" | When introducing results (overused but standard) |
| "zero-shot generalizability" | When your method transfers without retraining |

---

## Paper 2: DoG — Li et al. (2024)

**Full title:** Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs through Generation of Well-Formed Chains
**Venue:** EMNLP 2024
**File:** papers/Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs through Generation of Well-Formed Chains.pdf

### Human-Term Summary

Like GCR, DoG wants LLMs to reason on knowledge graphs without making things up. Their key move is defining a concept called a "well-formed chain" — a sequence of KG triples where each triple connects to the previous one. This is both the principle and the constraint.

Two threads of prior work exist: (1) retrieve a subgraph and let the LLM pick from it, (2) let the LLM interact with the KG step by step. Thread 1 doesn't deeply involve the LLM in graph reasoning. Thread 2 demands too much from small LLMs.

DoG's approach: give the LLM the entire question graph, use constrained decoding to force each generated step to be a valid triple from the graph, and let the subgraph expand as reasoning proceeds. They also use beam search at the triple level to avoid error propagation.

Key result: DoG beats both retrieval-based and agent-based methods, works with small open-source LLMs (8B parameters), and is training-free. But it needs the full graph as input, which requires a large context window.

### Sentence Patterns

**Opening with existing work's weakness:**
```
Knowledge Graphs (KGs) can serve as reliable knowledge sources for question answering
(QA) due to their structured representation of knowledge. Existing research on the
utilization of KG for large language models (LLMs) prevalently relies on subgraph
retriever or iterative prompting, overlooking the potential synergy of LLMs' step-wise
reasoning capabilities and KGs' structural nature.
```
Pattern: `[X] can serve as [Y]. Existing research [does Z], overlooking [MISSING THING].`

**Defining a concept as the paper's core:**
```
We first define a concept, well-formed chain, which consists of a sequence of
interrelated fact triplets on the KGs, starting from question entities and leading
to answers. We argue that this concept can serve as a principle for making faithful
and sound reasoning for KGQA.
```
Pattern: `We first define a concept, [NAME], which [DEFINITION]. We argue that this concept can serve as [ROLE].`

**Motivated by this:**
```
Motivated by this, we first define a concept, well-formed chain, to serve as a
principle for making faithful and sound reasoning on KGs.
```
Pattern: `Motivated by this, we [ACTION] to serve as [PRINCIPLE].`

**Explaining the constraint mechanism:**
```
By restricting the scope of valid tokens as output, this hard constraint is able to
strictly regularize the LLM's generation to be a well-formed chain.
```
Pattern: `By [RESTRICTING ACTION], this [TYPE] constraint is able to [EFFECT].`

**Results as bold claim:**
```
DoG effectively guarantees the generation of well-formed chains, thereby leading to
higher accuracy.
```
Pattern: `[METHOD] effectively [GUARANTEE], thereby leading to [RESULT].`

**Limitations as honest admission:**
```
While DoG demonstrates notable performance on KGQA task through training-free
graph-aware constrained decoding, there are some limitations to consider. First,
unlike specialized subgraph retrievers and iterative LLM-based prompting approaches,
DoG processes the entire question graph as input... This, however, requires a larger
context window in LLMs.
```
Pattern: `While [METHOD] demonstrates [positive], there are some limitations to consider. First, [limitation]. This, however, [consequence].`

### Grammar Structures

1. **Definition-first structure:**
   - Define concept → argue for its properties → build method around it
   - "A well-formed chain... is composed of... and each step of triplet can only grow from..."

2. **Two-thread problem framing:**
   - Thread 1: [approach] → [limitation]
   - Thread 2: [approach] → [limitation]
   - Therefore: [your approach]

3. **Property enumeration with semicolons:**
   - "Thanks to its properties, for a question, a well-formed chain offers a reasoning trajectory that is sound and faithful to the KG; Moreover, it will also naturally narrow down the search scopes..."

4. **Causal chain with "thereby":**
   - "DoG effectively guarantees the generation of well-formed chains, thereby leading to higher accuracy."

### Wording Choices to Borrow

| Their phrasing | When to use it |
|---|---|
| "overlooking the potential synergy of" | When critiquing prior work's blind spot |
| "We argue that this concept can serve as" | When proposing a new principle |
| "Motivated by this" | When transitioning from insight to method |
| "this hard constraint is able to strictly regularize" | When describing constrained decoding |
| "training-free approach" | When emphasizing no fine-tuning needed |
| "sound and faithful to the KG" | When describing what your method guarantees |
| "there are some limitations to consider" | Humble limitation intro (better than "The limitation is") |
| "this, however, requires" | When acknowledging a cost honestly |
| "thereby leading to" | When describing causal downstream effects |
| "the key contributions of this work are:" | Contribution list intro (alternative to GCR's version) |

---

## Paper 3: GCD — Geng et al. (2024)

**Full title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning
**Venue:** ICLR 2024
**File:** papers/Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning.pdf

### Human-Term Summary

LLMs are bad at generating structured output (like JSON, parse trees, entity lists) when they haven't been specifically fine-tuned for the task. Grammar-constrained decoding (GCD) fixes this by using a formal grammar to block invalid tokens during generation.

Previous constrained decoding work was task-specific (one system for parsing, another for code, another for entity linking). GCD's contribution: show that a single grammar formalism can handle all of these tasks. You just write a grammar for your task, and the decoder enforces it.

They introduce "input-dependent grammars" where the grammar changes based on the input (e.g., for entity disambiguation, the valid entities depend on the input text). They test on three tasks: closed information extraction, entity disambiguation, and constituency parsing.

Key result: grammar-constrained LLaMA-33B beats task-specific fine-tuned models on information extraction and entity disambiguation, without any fine-tuning. On parsing, it guarantees valid output trees but doesn't match supervised accuracy.

The paper is notable for its opinionated "Best practices for GCD" section and honest limitations about API incompatibility and latency.

### Sentence Patterns

**Opening with the problem framed as tension:**
```
Despite their impressive performance, large language models (LMs) still struggle with
reliably generating complex output structures when not finetuned to follow the required
output format exactly.
```
Pattern: `Despite their impressive performance, [X] still struggle with [PROBLEM] when [CONDITION].`

**Unifying claim:**
```
In this work, we demonstrate that formal grammars can describe the output space for a
much wider range of tasks and argue that GCD can serve as a unified framework for
structured NLP tasks in general.
```
Pattern: `In this work, we demonstrate that [X] can [BROAD CLAIM] and argue that [METHOD] can serve as [FRAMEWORK ROLE].`

**Practical vision:**
```
We envision GCD to be as simple to use as regular expressions, in the sense that the
user can specify a desired output structure in a declarative way, and the LM-generated
sequences will be guaranteed to be valid.
```
Pattern: `We envision [METHOD] to be as [COMPARISON], in the sense that [SIMPLIFIED DESCRIPTION].`

**Results as contrast:**
```
Our results indicate that grammar-constrained LMs substantially outperform unconstrained
LMs or even beat task-specific finetuned models.
```
Pattern: `Our results indicate that [METHOD] substantially outperform [BASELINE] or even beat [SURPRISING COMPARISON].`

**Honest limitation:**
```
Whereas unconstrained LLaMA models perform poorly, GCD (either input-dependent [IDG]
or input-independent [IIG]) significantly improves the performance of LLaMA. Although
there is still a gap with respect to the state-of-the-art model, GENRE [cite],
grammar-constrained LLaMA-33B performs better than a version of GENRE trained only on
the AIDA dataset (without pretraining on Wikipedia).
```
Pattern: `Whereas [BASELINE] [fails], [METHOD] significantly improves [METRIC]. Although there is still a gap with respect to [SOTA], [METHOD] performs better than [FAIR COMPARISON].`

**Best practices as opinionated list:**
```
We conclude with considerations regarding the effective use of GCD.
1. GCD is more effective with larger LLMs. When possible, use the largest available LLM.
2. Grammars should be as restrictive as possible. Consider using input-dependent grammars.
```
Pattern: Numbered list of concrete, opinionated recommendations.

### Grammar Structures

1. **"We show that" for demonstrations:**
   - "We show that, for a much wider range of NLP tasks, the respective output space can be described with a formal grammar"
   - "We show that, by combining GCD with powerful LLMs, we achieve remarkable improvements"

2. **Contrastive framing:**
   - "Whereas LMs excel at generating free-form text, they are not specifically designed for structured prediction tasks"
   - "This is in contrast to previous work, where the constraints were expressed in the form of finite-state automata"

3. **List structure for contributions:**
   - Numbered list (1), (2), (3) with each item stating a specific contribution

4. **Limitations as separate labeled sections:**
   - "Compatibility with API-based LLMs" then "Latency" — each limitation gets its own subheading

### Wording Choices to Borrow

| Their phrasing | When to use it |
|---|---|
| "Despite their impressive performance" | Opening gambit (positive → negative) |
| "In this work, we demonstrate that" | When making a broad claim about your contribution |
| "argue that [X] can serve as a unified framework" | When positioning your method as general |
| "We envision [X] to be as simple as" | When describing the practical aspiration |
| "substantially outperform" | When reporting strong results |
| "Although there is still a gap with respect to" | Honest acknowledgment without self-deprecation |
| "This is not surprising, since" | When a result is expected and you can explain why |
| "We conclude with considerations regarding" | When introducing best practices / discussion |
| "hold great promise for" | When describing future potential (use sparingly) |
| "especially where [X] is scarce or [Y] is expensive" | When motivating practical value |

---

## Cross-Paper Pattern Bank for DCA-Trie Writing

### Sentence Openers

| Purpose | Pattern | Source |
|---|---|---|
| Open with positive-then-negative | "Despite their impressive performance, [X] still struggle with [PROBLEM]" | GCD |
| Open with instability | "[X] can serve as [Y]. Existing research [does Z], overlooking [MISSING]" | DoG |
| Open with problem framing | "[X] have shown [positive], but they still struggle with [negative] due to [cause]" | GCR |
| Transition to method | "To this end, we introduce [NAME], a novel [TYPE] that [WHAT]" | GCR |
| Transition from insight | "Motivated by this, we [ACTION] to serve as [PRINCIPLE]" | DoG |
| Introduce unifying claim | "In this work, we demonstrate that [X] can [BROAD CLAIM]" | GCD |
| Introduce concept | "We first define a concept, [NAME], which [DEFINITION]" | DoG |

### Method Explanation Patterns

| Purpose | Pattern |
|---|---|
| Explain mechanism | "Inspired by [INSIGHT], we [ACTION]. This enables [CAPABILITY]." |
| Explain constraint | "By restricting [X], this [TYPE] constraint is able to [EFFECT]." |
| Explain integration | "In this way, [A] combines [STRENGTH OF A] with [STRENGTH OF B] to achieve [GOAL]." |
| Explain causal chain | "[METHOD] effectively [GUARANTEE], thereby leading to [RESULT]." |
| Introduce equation | "formulated as:" / "can be formalized as:" |
| Define variables | "where [VAR] denotes [MEANING]" |

### Results Patterns

| Purpose | Pattern |
|---|---|
| Report strong result | "[METHOD] substantially outperform [BASELINE] or even beat [COMPARISON]." |
| Report result with explanation | "[METHOD] demonstrates [RESULT], which indicates [INTERPRETATION]. However, [LIMITATION]." |
| Report ablation | "By removing [COMPONENT], we [OBSERVE DROP], indicating [IMPORTANCE]." |
| Report tension | "[METHOD] achieves [X] but [Y] remains limited by [CAUSE]." |

### Limitation Patterns

| Purpose | Pattern |
|---|---|
| Honest admission | "While [METHOD] demonstrates [positive], there are some limitations to consider." |
| Specific limitation | "First, [LIMITATION]. This, however, [CONSEQUENCE]." |
| Fair comparison | "Although there is still a gap with respect to [SOTA], [METHOD] performs better than [FAIR BASELINE]." |
| Scope boundary | "[METHOD] is limited to [SCOPE], which [CONSEQUENCE]." |

### Wording Bank

| Concept | Phrasing options |
|---|---|
| Preventing hallucination | "eliminate hallucination" / "faithful reasoning" / "zero hallucination" / "grounded in KGs" |
| Constrained decoding | "graph-constrained decoding" / "hard constraint" / "regulate the decoding process" / "restrict the scope of valid tokens" |
| No fine-tuning | "training-free" / "without finetuning" / "without additional training" / "zero-shot generalizability" |
| Search space reduction | "reduce the searching space" / "narrow down the search scopes" / "prune the probability distribution" |
| KG structure | "structured knowledge in KGs" / "KG topology" / "graph structure" / "reasoning paths grounded in KGs" |
| LLM reasoning | "reasoning capabilities" / "step-wise reasoning" / "inductive reasoning" / "graph reasoning" |
| Contribution intro | "The main contributions of this work are as follows:" / "The key contributions of this work are:" / "Our contributions can be summarized as follows:" |
| Critique prior work | "overlooking [X]" / "encounter difficulties in [Y]" / "suffer from [Z]" / "necessitate [COST]" |

---

## How to Use This Document

Before writing any section of the DCA-Trie paper:

1. **Pick the section** you're writing (Intro, Method, Results, etc.)
2. **Look up the sentence patterns** for that section type in the bank above
3. **Adapt the pattern** to your specific claim — don't copy verbatim, restructure around your data
4. **Check the wording bank** for domain-specific phrasing
5. **Read the relevant section** from the canonical paper for tone calibration
6. **Apply the humanizing guide** rules (no triadic lists, no hedge-then-assert, etc.)

The goal is not to imitate these papers but to write at the same level of professional confidence they demonstrate, while avoiding the AI-tell patterns flagged in the humanizing prose guide.
