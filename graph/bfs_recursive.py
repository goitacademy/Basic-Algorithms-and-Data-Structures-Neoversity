from collections import deque

def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

# Представлення графа за допомогою списку суміжності
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Запуск рекурсивного алгоритму BFS
bfs_recursive(graph, deque(["A"]))





# import matplotlib.pyplot as plt
# import networkx as nx
# from collections import deque
#
# # Функція для малювання графа з відвіданими ребрами
# def draw_graph(graph, visited_edges):
#     G = nx.Graph()
#     for node, neighbors in graph.items():
#         for neighbor in neighbors:
#             G.add_edge(node, neighbor, color='blue')
#
#     pos = nx.spring_layout(G)
#     colors = [G[u][v]['color'] for u, v in G.edges()]
#     nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
#
#     for edge in visited_edges:
#         G[edge[0]][edge[1]]['color'] = 'red'
#
#     colors = [G[u][v]['color'] for u, v in G.edges()]
#     nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
#     plt.show()
#
# # Функція BFS з відображенням відвіданих ребер
# def bfs_recursive(graph, queue, visited=None, visited_edges=None):
#     # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
#     if visited is None:
#         visited = set()
#     # Перевіряємо, чи існує список відвіданих ребер, якщо ні, то ініціалізуємо новий
#     if visited_edges is None:
#         visited_edges = []
#     # Якщо черга порожня, завершуємо рекурсію
#     if not queue:
#         return
#     # Вилучаємо вершину з початку черги
#     vertex = queue.popleft()
#     # Перевіряємо, чи відвідували раніше дану вершину
#     if vertex not in visited:
#         # Якщо не відвідували, друкуємо вершину
#         print(vertex, end=" ")
#         # Додаємо вершину до множини відвіданих вершин
#         visited.add(vertex)
#         # Додаємо невідвіданих сусідів даної вершини в кінець черги та додаємо ребро до списку відвіданих ребер
#         for neighbor in set(graph[vertex]) - visited:
#             queue.append(neighbor)
#             visited_edges.append((vertex, neighbor))
#             print(f"\nVisited edge: {vertex} -> {neighbor}")  # Друкуємо ребро
#             draw_graph(graph, visited_edges)  # Малюємо граф з оновленими ребрами
#     # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
#     bfs_recursive(graph, queue, visited, visited_edges)
#
# # Представлення графа за допомогою списку суміжності
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D", "E"],
#     "C": ["A", "F"],
#     "D": ["B"],
#     "E": ["B", "F"],
#     "F": ["C", "E"],
# }
#
# # Запуск рекурсивного алгоритму BFS
# bfs_recursive(graph, deque(["A"]))
