# DCA-Trie Interactive Demo

An interactive web interface for demonstrating the DCA-Trie system.

## Quick Start

### Option 1: Demo Mode (No GPU Required)

```bash
# Install Gradio
pip install gradio

# Run the demo
python experiments/type_oracle_full/demo/app.py

# Access at: http://localhost:7860
```

### Option 2: Live Mode (Requires GPU)

```bash
# SSH into Vast.ai
ssh -p 16354 root@ssh2.vast.ai

# Navigate to project
cd /workspace/graph-constrained-reasoning

# Pull latest changes
git pull origin claude/fix-decoding-pipeline

# Install Gradio
pip install gradio

# Run with live inference
python experiments/type_oracle_full/demo/app.py --live

# Access at: http://localhost:7860
```

### Option 3: Public URL (For Defense)

```bash
# Run with --share to create a public URL
python experiments/type_oracle_full/demo/app.py --share
```

This will generate a public URL you can share with your committee.

## Features

### Demo Mode
- **Pre-computed results** for 5 sample questions
- **Side-by-side comparison** of GCR vs DCA-Trie
- **Statistics panel** showing path reduction
- **No GPU required** — works on any machine

### Live Mode
- **Actual inference** using the Llama-3.1-8B model
- **Real-time results** for any question
- **Requires GPU** — run on Vast.ai

### About Tab
- **Method explanation** — how DCA-Trie works
- **Results summary** — key metrics
- **Citation info** — for academic use

## Sample Questions

| # | Question | Difficulty | Category |
|---|----------|------------|----------|
| 1 | What language is spoken in Jamaica? | Easy (1-hop) | Location |
| 2 | Where was Albert Einstein born? | Easy (1-hop) | Person |
| 3 | Who was the vice president before George W. Bush? | Medium (2-hop) | Government |
| 4 | What is the capital of France? | Easy (1-hop) | Location |
| 5 | Who directed the movie Inception? | Medium (2-hop) | Film |

## What the Demo Shows

1. **Reasoning Transparency**: Shows all candidate paths the model considers
2. **Filtering Effect**: Compare GCR (all paths) vs DCA (filtered paths)
3. **Path Reduction**: Typically 14.5% of paths are filtered
4. **Faithfulness**: Every path is a valid KG path
5. **Same Answers**: Both methods produce correct answers

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `gradio not found` | Run `pip install gradio` |
| `model not found` | Ensure you have the GCR model checkpoint |
| `CUDA out of memory` | Use a GPU with more VRAM |
| `Port in use` | Try `--port 7861` |

## Files

- `app.py` — Main Gradio application
- `sample_questions.json` — Pre-loaded questions
- `README.md` — This file

## For Defense

When presenting, focus on:

1. **Live demo**: Show a question being answered in real-time
2. **Comparison**: Show GCR vs DCA-Trie side-by-side
3. **Statistics**: Highlight the 14.5% path reduction
4. **Key insight**: "Tighter oracles don't guarantee higher accuracy"

## Related Documents

- [Objectives and Demo Design](../../../FINAL_PROJECT/OBJECTIVES_AND_DEMO.md)
- [Evaluation Metrics](../../../FINAL_PROJECT/docs/EVALUATION_METRICS.md)
- [Experiment Results](../../../FINAL_PROJECT/docs/EXPERIMENT_RESULTS.md)

---

*Created: July 16, 2026*
*For: Final Year Project Defense*
