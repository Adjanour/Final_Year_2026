#!/usr/bin/env python3
"""Generate figures for Chapter 4 of the DCA-Trie thesis."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Output directory
outdir = '/home/bernard/research/projects/FINAL_PROJECT/chapters/introduction/figures'
os.makedirs(outdir, exist_ok=True)

# Consistent style
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'axes.edgecolor': '#333333',
    'axes.linewidth': 1.2,
    'grid.color': '#333333',
    'grid.linewidth': 0.8,
    'grid.alpha': 0.7,
})

# =============================================================================
# Figure 1: Accuracy comparison across methods (grouped bar chart)
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 5))

methods = ['GCR\nBaseline', 'DCA-Trie\nv1', 'DCA-Trie\nv2*']
metrics = {
    'Hits@1': [91.6, 86.4, 54.9],
    'Accuracy': [77.7, 72.2, 31.8],
    'F1': [66.2, 61.6, 35.8],
}

x = np.arange(len(methods))
width = 0.25
colors = ['#2196F3', '#4CAF50', '#FF9800']

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width, values, width, label=metric, color=colors[i], edgecolor='white', linewidth=0.5)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.8,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Score (%)')
ax.set_xticks(x + width)
ax.set_xticklabels(methods)
ax.set_ylim(0, 105)
ax.legend(loc='upper right')
ax.set_title('Accuracy, Hits@1, and F1 by Method')
ax.yaxis.grid(True, color='#333333', alpha=0.7, linewidth=0.8)

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_accuracy_comparison.pdf'))
fig.savefig(os.path.join(outdir, 'fig_accuracy_comparison.png'))
plt.close(fig)
print("Created fig_accuracy_comparison")

# =============================================================================
# Figure 2: Path statistics (before vs after filtering)
# =============================================================================
fig, ax = plt.subplots(figsize=(6, 4.5))

categories = ['Total Paths\n(millions)', 'Avg Paths\nper Question']
before = [4.103, 2522]
after = [3.509, 2157]

x = np.arange(len(categories))
width = 0.3

bars1 = ax.bar(x - width/2, before, width, label='Before TypeOracle', color='#2196F3', edgecolor='white')
bars2 = ax.bar(x + width/2, after, width, label='After TypeOracle', color='#FF9800', edgecolor='white')

for bar, val in zip(bars1, before):
    label = f'{val:.1f}M' if val < 10 else f'{val:,.0f}'
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 30,
            label, ha='center', va='bottom', fontsize=10)
for bar, val in zip(bars2, after):
    label = f'{val:.1f}M' if val < 10 else f'{val:,.0f}'
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 30,
            label, ha='center', va='bottom', fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('Count')
ax.set_title('Path Statistics Before and After TypeOracle Filtering')
ax.legend()

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_path_statistics.pdf'))
fig.savefig(os.path.join(outdir, 'fig_path_statistics.png'))
plt.close(fig)
print("Created fig_path_statistics")

# =============================================================================
# Figure 3: Gate decomposition (pie chart)
# =============================================================================
fig, ax = plt.subplots(figsize=(5, 5))

labels = ['Range Gate\n(3.8%)', 'Type Gate\n(10.6%)', 'Admitted\n(85.5%)']
sizes = [3.8, 10.6, 85.5]
colors_pie = ['#FF9800', '#F44336', '#4CAF50']
explode = (0.05, 0.05, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie,
                                   autopct='', startangle=90, textprops={'fontsize': 11})
ax.set_title('TypeOracle Path Reduction by Gate')

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_gate_decomposition.pdf'))
fig.savefig(os.path.join(outdir, 'fig_gate_decomposition.png'))
plt.close(fig)
print("Created fig_gate_decomposition")

# =============================================================================
# Figure 4: FNR by gate (horizontal bar)
# =============================================================================
fig, ax = plt.subplots(figsize=(6, 3))

gates = ['Type Gate', 'Range Gate']
fnr = [3.3, 2.9]
threshold = 5.0

bars = ax.barh(gates, fnr, color=['#F44336', '#FF9800'], edgecolor='white', height=0.5)
ax.axvline(x=threshold, color='green', linestyle='--', linewidth=1.5, label=f'Target threshold ({threshold}%)')

for bar, val in zip(bars, fnr):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2.,
            f'{val}%', ha='left', va='center', fontsize=11)

ax.set_xlabel('False Negative Rate (%)')
ax.set_title('False Negative Rates by Gate (Target < 5%)')
ax.set_xlim(0, 7)
ax.legend(loc='lower right')

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_fnr_by_gate.pdf'))
fig.savefig(os.path.join(outdir, 'fig_fnr_by_gate.png'))
plt.close(fig)
print("Created fig_fnr_by_gate")

# =============================================================================
# Figure 5: Accuracy deltas (waterfall-style)
# =============================================================================
fig, ax = plt.subplots(figsize=(7, 4.5))

metrics_names = ['Hits@1', 'Accuracy', 'F1', 'Precision', 'Recall']
deltas = [-5.2, -5.5, -4.6, -4.4, -5.5]

colors_delta = ['#F44336' if d < 0 else '#4CAF50' for d in deltas]
bars = ax.bar(metrics_names, deltas, color=colors_delta, edgecolor='white', width=0.6)

for bar, val in zip(bars, deltas):
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., y - 0.3,
            f'{val:+.1f} pp', ha='center', va='top', fontsize=10, fontweight='bold')

ax.axhline(y=0, color='black', linewidth=0.8)
ax.set_ylabel('Change (percentage points)')
ax.set_title('Accuracy Deltas: DCA-Trie v1 vs GCR Baseline')
ax.yaxis.grid(True, color='#333333', alpha=0.7, linewidth=0.8)

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_accuracy_deltas.pdf'))
fig.savefig(os.path.join(outdir, 'fig_accuracy_deltas.png'))
plt.close(fig)
print("Created fig_accuracy_deltas")

# =============================================================================
# Figure 6: Execution time comparison
# =============================================================================
fig, ax = plt.subplots(figsize=(6, 4.5))

methods_time = ['GCR\nBaseline', 'DCA-Trie\nv1', 'DCA-Trie\nv2*']
total_time = [10329, 10385, 7945]
avg_time = [6.35, 6.38, 5.42]

x = np.arange(len(methods_time))
width = 0.35

bars1 = ax.bar(x - width/2, [t/3600 for t in total_time], width, label='Total (hours)', color='#2196F3', edgecolor='white')
ax2 = ax.twinx()
bars2 = ax2.bar(x + width/2, avg_time, width, label='Avg/Question (s)', color='#FF9800', edgecolor='white')

ax.set_ylabel('Total Time (hours)')
ax2.set_ylabel('Avg Time per Question (seconds)')
ax.set_xticks(x)
ax.set_xticklabels(methods_time)
ax.set_ylim(0, 4)
ax2.set_ylim(0, 8)

# Combined legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

ax.set_title('Execution Time by Method')

fig.tight_layout()
fig.savefig(os.path.join(outdir, 'fig_execution_time.pdf'))
fig.savefig(os.path.join(outdir, 'fig_execution_time.png'))
plt.close(fig)
print("Created fig_execution_time")

print("\nAll figures generated successfully.")
