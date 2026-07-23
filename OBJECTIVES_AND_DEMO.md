# Thesis Objectives Status & Demo Design

## Objectives Status Tracker

| # | Objective | Status | Evidence | Notes |
|---|-----------|--------|----------|-------|
| i | Characterise permissiveness problem (SIR metric) | ✅ **COMPLETE** | Chapter 3, §3.4; Chapter 4, §4.4 | SIR defined, measured on WebQSP |
| ii | Design semantic relevance scoring mechanism | ✅ **COMPLETE** | Chapter 3, §3.5; TypeOracle | Three approaches documented, TypeOracle chosen |
| iii | Implement DCA-Trie v1 (static filtering) | ✅ **COMPLETE** | `experiments/type_oracle_full/` | Working implementation, 14.5% reduction |
| iv | Implement DCA-Trie v2 (dynamic expansion) | ✅ **COMPLETE** | `experiments/type_oracle_full/decoding.py` | Implemented, interrupted run |
| v | Evaluate on WebQSP and CWQ | ⚠️ **PARTIAL** | Chapter 4 | WebQSP done; CWQ pending |
| vi | Demonstrate through interactive prototype | ❌ **NOT STARTED** | — | **This is what we need to build** |

---

## Gap Analysis

### What's Done
- ✅ Literature review (Chapter 2)
- ✅ Methodology (Chapter 3) — all three oracle designs documented
- ✅ WebQSP evaluation (Chapter 4) — complete with all metrics
- ✅ Non-monotone finding documented
- ✅ Statistical significance tests
- ✅ Timing analysis

### What's Missing
1. **CWQ results** — need to run on Vast.ai
2. **Interactive prototype** — objective (vi)
3. **Chapter 5 revisions** — needs to reference demo

### What Needs Updating
1. Chapter 1 — add reference to demo system
2. Chapter 4 — add CWQ results when available
3. Chapter 5 — reference demo as contribution

---

## Demo Design: Interactive DCA-Trie Prototype

### Why a Demo?

Objective (vi) requires:
> "to demonstrate DCA-Trie in practice through an interactive prototype system — either a web-based or command-line QA interface — allowing users to submit complex natural language questions and receive fact-grounded reasoning chains"

### Design Options

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **Web UI (Gradio)** | Visual, presentable, easy to demo | Requires GPU for inference | ⭐ **Best for defense** |
| **CLI tool** | Simple, fast to build | Less impressive visually | Good fallback |
| **Jupyter notebook** | Interactive, code visible | Not standalone | Good for appendix |
| **Visualization only** | Shows concepts clearly | No live inference | Good supplement |

### Recommended: Gradio Web Interface

**Why Gradio?**
- One-file Python app
- Runs on Vast.ai (GPU available)
- Shareable via public URL
- Visual output with reasoning chains
- Can show trie visualization

---

## Demo Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Gradio Web Interface                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Input Box   │  │ Run Button  │  │ Output Panel        │ │
│  │ (question)  │  │             │  │ - Reasoning paths   │ │
│  │             │  │             │  │ - Answer            │ │
│  │             │  │             │  │ - Path stats        │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    DCA-Trie Pipeline                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │ Entity       │  │ TypeOracle   │  │ Constrained      │  │
│  │ Linking      │→ │ Filtering    │→ │ Decoding         │  │
│  │              │  │ (range+type) │  │ (trie-based)     │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Knowledge Graph (Freebase)                │
│  • Question entities                                        │
│  • Candidate paths (before/after filtering)                 │
│  • Reasoning chains                                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Demo Features

### Core Features (Must Have)

1. **Question Input**: User types a natural language question
2. **Mode Selection**: GCR Baseline vs DCA-Trie v1
3. **Reasoning Output**: Shows generated reasoning paths
4. **Answer Display**: Shows final answer
5. **Statistics Panel**: Shows path counts, filtering stats

### Visualization Features (Nice to Have)

6. **Path Visualization**: Shows the KG path as a graph
7. **Filtering Animation**: Shows paths being filtered by TypeOracle
8. **Comparison View**: Side-by-side GCR vs DCA-Trie
9. **Confidence Scores**: Shows LLM confidence for each path

### Technical Features

10. **Sample Questions**: Pre-loaded example questions
11. **Export Results**: Download reasoning chains as JSON
12. **Error Handling**: Graceful fallback for edge cases

---

## Demo Implementation Plan

### File Structure

```
experiments/type_oracle_full/demo/
├── app.py                  # Main Gradio app
├── requirements.txt        # Dependencies
├── sample_questions.json   # Pre-loaded questions
├── static/
│   └── style.css          # Custom styling
└── README.md              # How to run
```

### Key Components

1. **`app.py`**: Main Gradio interface
   - Loads model once at startup
   - Provides `predict(question, mode)` function
   - Returns reasoning paths + answer + stats

2. **`sample_questions.json`**: Pre-loaded questions
   - 10-15 diverse questions
   - Covers different hop depths
   - Shows filtering effect

3. **Visualization**: Optional matplotlib plots
   - Path reduction bar chart
   - Filtering breakdown pie chart

---

## Demo Questions (Pre-loaded)

```json
{
  "questions": [
    {
      "text": "What language is spoken in Jamaica?",
      "expected_paths": 2,
      "difficulty": "easy"
    },
    {
      "text": "Who was the vice president of the United States before George W. Bush?",
      "expected_paths": 3,
      "difficulty": "medium"
    },
    {
      "text": "What awards did the director of Inception win?",
      "expected_paths": 5,
      "difficulty": "hard"
    },
    {
      "text": "Where was Albert Einstein born?",
      "expected_paths": 1,
      "difficulty": "easy"
    },
    {
      "text": "What is the capital of the country where the Amazon rainforest is located?",
      "expected_paths": 4,
      "difficulty": "medium"
    }
  ]
}
```

---

## Running the Demo

### On Vast.ai

```bash
# SSH into Vast.ai
ssh -p 16354 root@ssh2.vast.ai

# Navigate to project
cd /workspace/graph-constrained-reasoning

# Pull latest changes
git pull origin claude/fix-decoding-pipeline

# Install Gradio
pip install gradio

# Run the demo
python experiments/type_oracle_full/demo/app.py

# Access at: http://localhost:7860
```

### Make Public (for defense)

```bash
# Gradio automatically creates a public URL
# Share the URL with your committee
```

---

## What the Demo Shows

### For the Committee

1. **Live Inference**: Question → Answer in real-time
2. **Reasoning Transparency**: Shows all reasoning paths
3. **Filtering Effect**: Compare GCR (all paths) vs DCA (filtered paths)
4. **Faithfulness**: Every path is a valid KG path
5. **Non-monotone**: Can see how filtering affects results

### Key Talking Points

> "This demo shows our DCA-Trie system in action. On the left, you see the GCR baseline with all candidate paths. On the right, you see DCA-Trie with TypeOracle filtering. Notice how DCA-Trie removes irrelevant paths but still generates the correct answer."

> "The statistics panel shows the path reduction — typically 14.5% of paths are filtered out. This demonstrates Condition R (Semantic Relevance Reduction) from our methodology."

---

## Timeline

| Task | Time | Priority |
|------|------|----------|
| Create demo directory structure | 30 min | High |
| Write `app.py` with Gradio | 2 hours | High |
| Add sample questions | 30 min | High |
| Test on Vast.ai | 1 hour | High |
| Add visualizations | 1 hour | Medium |
| Write README | 30 min | Medium |
| Practice demo for defense | 1 hour | High |
| **Total** | **~6 hours** | — |

---

## Next Steps

1. **Build the demo** (today)
2. **Run CWQ experiment** (on Vast.ai)
3. **Update Chapter 1** (add demo reference)
4. **Update Chapter 5** (add demo as contribution)
5. **Practice defense** (with demo)

---

*Created: July 16, 2026*
*Status: Ready to build demo*
