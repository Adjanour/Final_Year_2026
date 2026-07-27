"""
DCA-Trie Algorithm Visualization
================================
Step-by-step visualization of how TypeOracle filters knowledge graph paths.

Usage:
    python visualize_algorithm.py

Access at: http://localhost:7861
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================================
# Example Knowledge Graph Data
# ============================================================================

# Example: "What language is spoken in Jamaica?"
EXAMPLE_KG = {
    "question": "What language is spoken in Jamaica?",
    "entities": ["Jamaica"],
    "nodes": [
        {"id": "Jamaica", "type": "Country", "label": "Jamaica"},
        {"id": "Jamaican_Creole", "type": "Language", "label": "Jamaican Creole English"},
        {"id": "Jamaican_English", "type": "Language", "label": "Jamaican English"},
        {"id": "Jamaican_dollar", "type": "Currency", "label": "Jamaican dollar"},
        {"id": "USD", "type": "Currency", "label": "US dollar"},
        {"id": "Kingston", "type": "City", "label": "Kingston"},
        {"id": "Caribbean", "type": "Region", "label": "Caribbean"},
        {"id": "English", "type": "Language", "label": "English"},
        {"id": "Spanish", "type": "Language", "label": "Spanish"},
    ],
    "edges": [
        {"source": "Jamaica", "target": "Jamaican_Creole", "relation": "languages_spoken"},
        {"source": "Jamaica", "target": "Jamaican_English", "relation": "languages_spoken"},
        {"source": "Jamaica", "target": "English", "relation": "official_language"},
        {"source": "Jamaica", "target": "Spanish", "relation": "languages_spoken"},
        {"source": "Jamaica", "target": "Jamaican_dollar", "relation": "currency_used"},
        {"source": "Jamaica", "target": "Kingston", "relation": "capital"},
        {"source": "Jamaica", "target": "Caribbean", "relation": "containedby"},
        {"source": "Jamaican_dollar", "target": "USD", "relation": "exchange_rate"},
    ],
    "all_paths": [
        {"id": 1, "hops": [("Jamaica", "languages_spoken", "Jamaican_Creole")], "terminal": "Jamaican_Creole", "terminal_type": "Language"},
        {"id": 2, "hops": [("Jamaica", "languages_spoken", "Jamaican_English")], "terminal": "Jamaican_English", "terminal_type": "Language"},
        {"id": 3, "hops": [("Jamaica", "official_language", "English")], "terminal": "English", "terminal_type": "Language"},
        {"id": 4, "hops": [("Jamaica", "languages_spoken", "Spanish")], "terminal": "Spanish", "terminal_type": "Language"},
        {"id": 5, "hops": [("Jamaica", "currency_used", "Jamaican_dollar")], "terminal": "Jamaican_dollar", "terminal_type": "Currency"},
        {"id": 6, "hops": [("Jamaica", "currency_used", "Jamaican_dollar"), ("Jamaican_dollar", "exchange_rate", "USD")], "terminal": "USD", "terminal_type": "Currency"},
        {"id": 7, "hops": [("Jamaica", "capital", "Kingston")], "terminal": "Kingston", "terminal_type": "City"},
        {"id": 8, "hops": [("Jamaica", "containedby", "Caribbean")], "terminal": "Caribbean", "terminal_type": "Region"},
    ],
    "answer_types": ["Language"],
    "oracle_decisions": {
        1: {"range_gate": True, "type_gate": True, "admitted": True, "reason": "languages_spoken range includes Language; terminal type matches Language"},
        2: {"range_gate": True, "type_gate": True, "admitted": True, "reason": "languages_spoken range includes Language; terminal type matches Language"},
        3: {"range_gate": True, "type_gate": True, "admitted": True, "reason": "official_language range includes Language; terminal type matches Language"},
        4: {"range_gate": True, "type_gate": True, "admitted": True, "reason": "languages_spoken range includes Language; terminal type matches Language"},
        5: {"range_gate": True, "type_gate": False, "admitted": False, "reason": "currency_used range includes Currency; terminal type Currency does NOT match Language"},
        6: {"range_gate": True, "type_gate": False, "admitted": False, "reason": "currency_used range includes Currency; terminal type Currency does NOT match Language"},
        7: {"range_gate": True, "type_gate": False, "admitted": False, "reason": "capital range includes City; terminal type City does NOT match Language"},
        8: {"range_gate": True, "type_gate": False, "admitted": False, "reason": "containedby range includes Region; terminal type Region does NOT match Language"},
    },
}


# ============================================================================
# Algorithm Steps
# ============================================================================

def generate_algorithm_steps(kg_data: dict) -> list:
    """Generate step-by-step algorithm visualization data."""
    steps = []
    
    # Step 1: Show the question and knowledge graph
    steps.append({
        "step": 1,
        "title": "Input: Question and Knowledge Graph",
        "description": f"Question: \"{kg_data['question']}\"\n\nThe knowledge graph contains {len(kg_data['nodes'])} entities and {len(kg_data['edges'])} relations. We need to find paths from the question entity to potential answers.",
        "highlight_nodes": kg_data["entities"],
        "highlight_edges": [],
        "filtered_paths": [],
        "admitted_paths": [],
    })
    
    # Step 2: Enumerate all paths (DFS)
    steps.append({
        "step": 2,
        "title": "Path Generation: DFS from Question Entity",
        "description": f"Starting from Jamaica, we enumerate all paths up to 2 hops:\n\n" + 
                       "\n".join([f"Path {p['id']}: {' -> '.join([f'{h[0]} -[{h[1]}]-> {h[2]}' for h in p['hops']])}" for p in kg_data["all_paths"]]) +
                       f"\n\nTotal: {len(kg_data['all_paths'])} paths generated",
        "highlight_nodes": kg_data["entities"],
        "highlight_edges": [e for e in kg_data["edges"]],
        "filtered_paths": [],
        "admitted_paths": [],
    })
    
    # Step 3: Infer answer types from question
    steps.append({
        "step": 3,
        "title": "Type Inference: What type of answer?",
        "description": f"From the question \"What language is spoken in Jamaica?\", we infer:\n\nAnswer types: {', '.join(kg_data['answer_types'])}\n\nThe TypeOracle will check if each path's terminal entity matches these types.",
        "highlight_nodes": kg_data["entities"],
        "highlight_edges": [],
        "filtered_paths": [],
        "admitted_paths": [],
    })
    
    # Step 4-11: Apply gates to each path
    for path in kg_data["all_paths"]:
        decision = kg_data["oracle_decisions"][path["id"]]
        path_desc = " -> ".join([f"{h[0]} -[{h[1]}]-> {h[2]}" for h in path["hops"]])
        
        if decision["admitted"]:
            status = "ADMITTED"
            detail = f"Range gate: PASS (relation '{path['hops'][-1][1]}' allows type '{path['terminal_type']}')\nType gate: PASS (terminal type '{path['terminal_type']}' matches answer type '{kg_data['answer_types'][0]}')"
        else:
            status = "FILTERED"
            detail = f"Range gate: PASS\nType gate: FAIL (terminal type '{path['terminal_type']}' does NOT match answer type '{kg_data['answer_types'][0]}')"
        
        steps.append({
            "step": 3 + path["id"],
            "title": f"Oracle Decision: Path {path['id']} - {status}",
            "description": f"Path: {path_desc}\n\nTerminal entity: {path['terminal']} (type: {path['terminal_type']})\n\n{detail}\n\nResult: {status}",
            "highlight_nodes": [path["hops"][-1][0], path["hops"][-1][2]],
            "highlight_edges": [(h[0], h[2]) for h in path["hops"]],
            "filtered_paths": [p["id"] for p in kg_data["all_paths"] if not kg_data["oracle_decisions"][p["id"]]["admitted"] and p["id"] <= path["id"]],
            "admitted_paths": [p["id"] for p in kg_data["all_paths"] if kg_data["oracle_decisions"][p["id"]]["admitted"] and p["id"] <= path["id"]],
        })
    
    # Final step: Summary
    admitted = [p for p in kg_data["all_paths"] if kg_data["oracle_decisions"][p["id"]]["admitted"]]
    filtered = [p for p in kg_data["all_paths"] if not kg_data["oracle_decisions"][p["id"]]["admitted"]]
    
    steps.append({
        "step": 12,
        "title": "Result: Filtered Path Set",
        "description": f"TypeOracle Filtering Complete\n\n" +
                       f"Paths admitted: {len(admitted)} / {len(kg_data['all_paths'])}\n" +
                       f"Paths filtered: {len(filtered)} / {len(kg_data['all_paths'])}\n" +
                       f"Reduction: {(1 - len(admitted)/len(kg_data['all_paths']))*100:.1f}%\n\n" +
                       "Admitted paths (will be in trie):\n" +
                       "\n".join([f"  Path {p['id']}: {' -> '.join([h[2] for h in p['hops']])}" for p in admitted]) +
                       "\n\nFiltered paths (removed from trie):\n" +
                       "\n".join([f"  Path {p['id']}: {' -> '.join([h[2] for h in p['hops']])}" for p in filtered]),
        "highlight_nodes": [],
        "highlight_edges": [],
        "filtered_paths": [p["id"] for p in filtered],
        "admitted_paths": [p["id"] for p in admitted],
    })
    
    return steps


# ============================================================================
# Gradio Visualization Interface
# ============================================================================

def create_visualization():
    """Create the algorithm visualization interface."""
    try:
        import gradio as gr
    except ImportError:
        print("Gradio not installed. Run: pip install gradio")
        return None
    
    steps = generate_algorithm_steps(EXAMPLE_KG)
    current_step = [0]  # Mutable state
    
    def get_step(step_idx):
        """Get data for a specific step."""
        if step_idx < 0 or step_idx >= len(steps):
            return "Invalid step", "", ""
        
        step = steps[step_idx]
        
        # Format step counter
        step_counter = f"Step {step['step']} / {len(steps)}"
        
        # Format title and description
        content = f"## {step['title']}\n\n{step['description']}"
        
        # Format graph visualization (text-based)
        graph_viz = format_kg_viz(step)
        
        # Format path status
        path_status = format_path_status(step)
        
        return step_counter, content, graph_viz, path_status
    
    def format_kg_viz(step):
        """Format knowledge graph visualization."""
        lines = ["### Knowledge Graph", ""]
        
        # Draw nodes
        lines.append("**Entities:**")
        for node in EXAMPLE_KG["nodes"]:
            marker = " <-- question" if node["id"] in EXAMPLE_KG["entities"] else ""
            lines.append(f"  [{node['type']}] {node['label']}{marker}")
        
        lines.append("")
        lines.append("**Relations:**")
        for edge in EXAMPLE_KG["edges"]:
            # Check if this edge is highlighted
            is_highlighted = (edge["source"], edge["target"]) in step.get("highlight_edges", [])
            marker = " *" if is_highlighted else ""
            lines.append(f"  {edge['source']} --[{edge['relation']}]--> {edge['target']}{marker}")
        
        if step.get("highlight_edges"):
            lines.append("")
            lines.append("* = currently being evaluated")
        
        return "\n".join(lines)
    
    def format_path_status(step):
        """Format path status table."""
        lines = ["### Path Status", ""]
        lines.append("| Path | Route | Terminal Type | Status |")
        lines.append("|------|-------|---------------|--------|")
        
        for path in EXAMPLE_KG["all_paths"]:
            route = " -> ".join([h[2] for h in path["hops"]])
            decision = EXAMPLE_KG["oracle_decisions"][path["id"]]
            
            if path["id"] in step.get("admitted_paths", []):
                status = "ADMITTED"
            elif path["id"] in step.get("filtered_paths", []):
                status = "FILTERED"
            else:
                status = "pending"
            
            lines.append(f"| {path['id']} | {route} | {path['terminal_type']} | {status} |")
        
        return "\n".join(lines)
    
    def next_step(current):
        """Advance to next step."""
        new_step = min(current + 1, len(steps) - 1)
        return new_step, get_step(new_step)
    
    def prev_step(current):
        """Go to previous step."""
        new_step = max(current - 1, 0)
        return new_step, get_step(new_step)
    
    def go_to_step(step_num):
        """Go to specific step."""
        new_step = max(0, min(step_num - 1, len(steps) - 1))
        return new_step, get_step(new_step)
    
    # Build interface
    with gr.Blocks(title="DCA-Trie Algorithm Visualization") as demo:
        gr.Markdown("""
        # DCA-Trie Algorithm Visualization
        
        Step-by-step walkthrough of how TypeOracle filters knowledge graph paths.
        
        **Example**: "What language is spoken in Jamaica?"
        """)
        
        with gr.Row():
            # Left panel: Controls and step content
            with gr.Column(scale=2):
                step_counter = gr.Markdown("Step 1 / 12")
                step_content = gr.Markdown()
                
                with gr.Row():
                    prev_btn = gr.Button("Previous")
                    next_btn = gr.Button("Next", variant="primary")
                
                step_input = gr.Number(
                    label="Go to step",
                    value=1,
                    minimum=1,
                    maximum=len(steps),
                )
                go_btn = gr.Button("Go")
            
            # Right panel: Graph and path status
            with gr.Column(scale=3):
                graph_viz = gr.Markdown()
                path_status = gr.Markdown()
        
        # Wire up controls
        prev_btn.click(
            fn=prev_step,
            inputs=[step_counter],
            outputs=[step_counter, step_content, graph_viz, path_status],
        )
        
        next_btn.click(
            fn=next_step,
            inputs=[step_counter],
            outputs=[step_counter, step_content, graph_viz, path_status],
        )
        
        go_btn.click(
            fn=go_to_step,
            inputs=[step_input],
            outputs=[step_counter, step_content, graph_viz, path_status],
        )
        
        # Load first step on startup
        demo.load(
            fn=lambda: get_step(0),
            outputs=[step_counter, step_content, graph_viz, path_status],
        )
    
    return demo


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DCA-Trie Algorithm Visualization")
    parser.add_argument("--port", type=int, default=7861, help="Port to run on")
    parser.add_argument("--share", action="store_true", help="Create public URL")
    args = parser.parse_args()
    
    # Create visualization
    demo = create_visualization()
    
    if demo is None:
        print("Failed to create visualization. Make sure gradio is installed.")
        sys.exit(1)
    
    # Launch
    print(f"\nStarting DCA-Trie Algorithm Visualization...")
    print(f"Local: http://localhost:{args.port}")
    if args.share:
        print(f"Public URL will be generated...")
    
    demo.launch(server_port=args.port, share=args.share)
