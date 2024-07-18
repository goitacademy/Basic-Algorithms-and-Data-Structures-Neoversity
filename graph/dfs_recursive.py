def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS
dfs_recursive(graph, 'A')





# import matplotlib.pyplot as plt
# import networkx as nx
#
# # Функція для візуалізації графа з кольоровими ребрами
# def draw_graph_step(graph, pos, visited_edges):
#     plt.figure()
#     G = nx.Graph(graph)
#     nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
#
#     red_edges = visited_edges
#     blue_edges = [(u, v) for u in graph for v in graph[u] if (u, v) not in visited_edges and (v, u) not in visited_edges]
#
#     nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=2)
#     nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='blue', width=2, style='dashed')
#
#     plt.show()
#
# # Функція для обхід графа з візуалізацією
# def dfs_recursive_visual(graph, vertex, visited=None, visited_edges=None, pos=None):
#     if visited is None:
#         visited = set()
#     if visited_edges is None:
#         visited_edges = []
#     if pos is None:
#         pos = nx.spring_layout(graph)  # Layout для графа
#
#     visited.add(vertex)
#     print(vertex, end=' ')  # Відвідуємо вершину
#
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             visited_edges.append((vertex, neighbor))
#             draw_graph_step(graph, pos, visited_edges)  # Візуалізація на кожному кроці
#             dfs_recursive_visual(graph, neighbor, visited, visited_edges, pos)
#
# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# # Створення об'єкта графа для networkx
# G = nx.Graph()
# for node, neighbors in graph.items():
#     for neighbor in neighbors:
#         G.add_edge(node, neighbor)
#
# # Виклик функції DFS з візуалізацією
# dfs_recursive_visual(graph, 'A')
