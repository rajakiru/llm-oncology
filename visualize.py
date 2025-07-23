import json
import networkx as nx
import matplotlib.pyplot as plt

# Load your KG triples
with open("data/toy_kg_nsclc.json") as f:
    triples = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
for t in triples:
    G.add_edge(t["source"], t["target"], label=t["relation"])

# Generate positions using a spaced-out spring layout
pos = nx.spring_layout(G, k=1.5, iterations=100, seed=42)

# Draw nodes and edges
plt.figure(figsize=(18, 12))
nx.draw(G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=4000,
        font_size=9,
        font_weight='bold',
        edge_color='gray',
        arrows=True,
        arrowstyle='-|>',
        arrowsize=20)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5)

# Final touches
plt.title("NSCLC Stage I Knowledge Graph", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()

