# Guide 4: Tools & Facilities — What We Used

## What This Section Covers

The software stack, hardware, and resources used in the project.

## Software Stack

| Tool | Purpose | Why this one |
| ------ | --------- | ------------- |
| **Python** | Main language | ML ecosystem |
| **PyTorch** | Deep learning framework | LLM inference |
| **HuggingFace Transformers** | LLM loading/inference | Standard for LLMs |
| **GCR codebase** | Baseline implementation | Direct comparison |
| **sentence-transformers** | Embedding computation | MiniLM-L6-v2 for semantic scoring |
| **NetworkX** | Graph operations | BFS, DFS, graph construction |
| **marisa-trie** | Prefix tree for constrained decoding | O(1) token lookup |
| **Freebase** | Knowledge graph | Via WebQSP and CWQ benchmarks |

## Hardware

| Resource | Specs | Used for |
|----------|-------|----------|
| **NVIDIA RTX 4090** | 24 GB VRAM | LLM inference (bfloat16) |
| **Google Colab** | Free GPU | Prototyping |
| **Local Linux workstation** | CPU | Data processing, analysis |

## Datasets

| Dataset | Size | Hops | Source |
|---------|------|------|--------|
| **WebQSP** | 1,628 test queries | 1-2 | Freebase |
| **CWQ** | 3,531 samples | up to 4 | Freebase |

## Key Libraries Explained

### marisa-trie

- A prefix tree (trie) implemented in C++ with Python bindings
- Stores tokenized paths as sequences of token IDs
- Lookup: given a prefix, return all valid next tokens in O(1)
- Why not regular dict? marisa-trie is memory-efficient and fast for large vocabularies

### NetworkX

- Graph library for Python
- We use it to:
  - Build directed graphs from KG triplets
  - Run BFS/DFS to enumerate paths
  - Find neighbours of entities

### sentence-transformers

- Pretrained models that convert text to fixed-size vectors
- We use `all-MiniLM-L6-v2` (384-dimensional)
- No fine-tuning needed — zero-shot semantic similarity

## If Asked

> **"What tools did you use?"**
> "Python, PyTorch, HuggingFace Transformers for LLM inference. NetworkX for graph operations, marisa-trie for the prefix tree constraint. We evaluated on WebQSP and CWQ benchmarks using Freebase."

> **"Why marisa-trie?"**
> "It gives O(1) valid next-token lookup, which is critical for constrained decoding. At each step, we need to instantly know which tokens the LLM is allowed to generate."

## Practice

1. Why did we use bfloat16 instead of float32 for inference?
2. What would happen if we used a regular Python dict instead of marisa-trie?
3. Why is sentence-transformers preferred over fine-tuning a custom encoder?
