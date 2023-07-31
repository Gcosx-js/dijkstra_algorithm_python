import networkx as nx
import matplotlib.pyplot as plt

def GraphVisualization(matris):
    class main:

        def __init__(self):
            self.visual = []
            self.node_labels = {}

        def addEdge(self, a, b, weight):
            temp = [a, b, weight]
            self.visual.append(temp)

        def visualize(self):
            G = nx.Graph()
            G.add_weighted_edges_from(self.visual)
            pos = nx.spring_layout(G)
            labels = nx.get_edge_attributes(G, 'weight')
            alphabet_labels = {i: i for i in G.nodes}
            self.node_labels = alphabet_labels

            nx.draw_networkx(G, pos, with_labels=True, labels=self.node_labels,
                             node_size=1000, node_color='skyblue', font_size=10, font_weight='bold',
                             edge_color='gray', width=2, alpha=0.8)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
            plt.title('Quliyev Elmir')
            plt.axis('off')
            plt.show()

    G = main()

    for i in range(len(matris)):
        for j in range(i + 1, len(matris)):
            if matris[i][j] > 0:
                G.addEdge(chr(65 + i), chr(65 + j), matris[i][j])

    G.visualize()