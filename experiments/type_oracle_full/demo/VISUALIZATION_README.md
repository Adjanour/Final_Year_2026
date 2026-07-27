# DCA-Trie Visualizations

Two visualization options for demonstrating the algorithm.

---

## Option 1: Standalone HTML (Recommended for Defense)

**File**: `visualize_algorithm.html`

**How to use**:
1. Open `visualize_algorithm.html` in any web browser
2. No server required, works offline
3. Use arrow keys or buttons to step through

**Features**:
- Interactive knowledge graph with SVG
- Step-by-step TypeOracle filtering
- Color-coded nodes (green=admitted, red=filtered)
- Path status table
- Real-time statistics

**Best for**: Presenting on your laptop during defense

---

## Option 2: Gradio App (For sharing online)

**File**: `visualize_algorithm.py`

**How to use**:
```bash
# Install Gradio
pip install gradio

# Run visualization
python experiments/type_oracle_full/demo/visualize_algorithm.py

# Access at: http://localhost:7861

# Share publicly
python experiments/type_oracle_full/demo/visualize_algorithm.py --share
```

**Best for**: Sharing URL with committee members

---

## What the Visualization Shows

### Algorithm Steps

| Step | Title | What Happens |
|------|-------|--------------|
| 1 | Input | Show question and KG |
| 2 | Path Generation | DFS enumerates all paths |
| 3 | Type Inference | Infer answer types from question |
| 4-10 | Oracle Decisions | Evaluate each path (range + type gate) |
| 11 | Result | Show final admitted/filtered sets |

### Visual Elements

- **Blue nodes**: Currently being evaluated
- **Green nodes**: Admitted by TypeOracle
- **Red nodes**: Filtered by TypeOracle
- **Gray nodes**: Not yet evaluated
- **Highlighted edges**: Currently being evaluated

### Example Flow

```
Question: "What language is spoken in Jamaica?"

Step 1:  Jamaica (blue) -- show all connections
Step 2:  Jamaica -> 7 paths generated
Step 3:  Answer type: Language
Step 4:  Jamaica -> Jamaican Creole [ADMITTED] (green)
Step 5:  Jamaica -> Jamaican English [ADMITTED] (green)
Step 6:  Jamaica -> English [ADMITTED] (green)
Step 7:  Jamaica -> Spanish [ADMITTED] (green)
Step 8:  Jamaica -> Jamaican dollar [FILTERED] (red)
Step 9:  Jamaica -> Kingston [FILTERED] (red)
Step 10: Jamaica -> Caribbean [FILTERED] (red)
Step 11: Result: 4 admitted, 3 filtered (42.9% reduction)
```

---

## For Defense Presentation

### How to Present

1. **Open HTML file** in full-screen browser
2. **Start at Step 1**: Explain the question and KG
3. **Click Next** through each step
4. **Pause at Step 3**: Explain answer type inference
5. **Step through 4-10**: Show each oracle decision
6. **End at Step 11**: Show final statistics

### Key Talking Points

- "Here we see the knowledge graph for 'What language is spoken in Jamaica?'"
- "The TypeOracle infers the answer type is 'Language'"
- "For each path, we check two gates: range and type"
- "Notice how paths 5-7 are filtered because their terminal types don't match"
- "This gives us a 42.9% reduction while keeping all correct answers"

### Backup Slides

If asked about specific paths, click to that step and explain:
- Why the range gate passed
- Why the type gate passed or failed
- What would happen with different answer types

---

## Files

- `visualize_algorithm.html` — Standalone HTML (no server needed)
- `visualize_algorithm.py` — Gradio version (needs server)
- `README.md` — This file

---

*For: Final Year Project Defense*
