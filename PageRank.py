import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a directed graph
G = nx.DiGraph()
edges = [("A", "B"), ("B", "C"), ("C", "A"), ("A", "D"), ("D", "C")]
G.add_edges_from(edges)

# Step 2: Calculate PageRank
pagerank_scores = nx.pagerank(G, alpha=0.85)

# Step 3: Print the scores
print("PageRank Scores:")
for node, score in pagerank_scores.items():
    print(f"{node}: {score:.4f}")

# Step 4: Visualize the graph
pos = nx.spring_layout(G)
node_sizes = [pagerank_scores[node] * 3000 for node in G.nodes]

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color='skyblue',
    font_size=12,
    arrows=True
)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}→{v}" for u, v in G.edges()}, font_size=10)
plt.title("Directed Graph with PageRank Node Sizes")
plt.show()
