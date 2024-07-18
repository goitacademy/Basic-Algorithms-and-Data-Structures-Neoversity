import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph() # неорієнтований граф
#
# G.add_node("A") # Добав вершину
# G.add_nodes_from(["B", "C", "D"]) # Добав вершини
# # G.add_edge("A", "B") # Добав ребро
# G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")]) # Добав ребра
# # G.remove_node("A")
# # G.remove_nodes_from(["B", "C", "D"])
# # G.remove_edge("A", "B")
# # G.remove_edges_from([("A", "C"), ("B", "C"), ("B", "D")])
# print(G.nodes())  # ['A', 'B', 'C', 'D']
# print(G.edges())  # [('A', 'C'), ('B', 'C'), ('B', 'D')]
# print(nx.is_connected(G))
#
# nx.draw(G, with_labels=True)
# plt.show()
#

# DG = nx.DiGraph() # орієнтований граф
# G = nx.Graph()
# G.add_edges_from([("A", "B"), ("B", "C")])
# DG = nx.DiGraph(G)
# nx.draw(DG, with_labels=True)
# plt.show()


# G = nx.complete_graph(8)  # створення повного графа
# nx.draw(G, with_labels=True)
# plt.show()


# G = nx.complete_graph(4)
# options = {
#     "node_color": "yellow",
#     "edge_color": "lightblue",
#     "node_size": 500,
#     "width": 3,
#     "with_labels": True
# }
# nx.draw(G, **options)
# plt.show()


# G = nx.complete_graph(8)
# pos = nx.circular_layout(G) # Кругове формування
# nx.draw(G, pos, with_labels=True)
# plt.title("Circular Layout")
# plt.show()



# G = nx.complete_graph(8)
# pos = nx.random_layout(G) # Випадкове формування
# nx.draw(G, pos, with_labels=True)
# plt.title("Random Layout")
# plt.show()

# G = nx.complete_graph(8)
# pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин у вигляді відносних кіл
# pos = nx.shell_layout(G, pos)
# nx.draw(G, pos, with_labels=True)
# plt.title("Shell Layout")
# plt.show()

# # Створення графа
# G = nx.Graph()
#
# # Додавання міст і доріг
# G.add_edge('A', 'B', weight=5)
# G.add_edge('A', 'C', weight=10)
# G.add_edge('B', 'D', weight=3)
# G.add_edge('C', 'D', weight=2)
# G.add_edge('D', 'E', weight=4)
#
# # Візуалізація графа
# pos = nx.spring_layout(G, seed=42)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#
# plt.show()

# # Створення графа
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# G = nx.Graph(graph)
#
# # DFS
# dfs_tree = nx.dfs_tree(G, source='A')
# print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A
# print(list(dfs_tree.nodes()))  # виведе вузли DFS-дерева з коренем у вузлі A
# # BFS
# bfs_tree = nx.bfs_tree(G, source='A')
# print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
# print(list(bfs_tree.nodes()))  # виведе вузли BFS-дерева з коренем у вузлі A