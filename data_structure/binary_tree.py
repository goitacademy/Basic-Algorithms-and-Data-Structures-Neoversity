print("TreeNode")
# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Визначаємо клас для вузлів дерева
# class TreeNode:
#     def __init__(self, value):
#         self.value = value  # Значення вузла
#         self.left = None  # Лівий дочірній вузол
#         self.right = None  # Правий дочірній вузол
#
# # Функція для вставки вузлів у бінарне дерево в рівневому порядку
# def insert_level_order(arr, root, i, n):
#     # Базовий випадок для рекурсії
#     if i < n:
#         temp = TreeNode(arr[i])  # Створюємо новий вузол з поточним значенням масиву
#         root = temp
#
#         # Вставляємо лівий дочірній вузол
#         root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
#
#         # Вставляємо правий дочірній вузол
#         root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
#
#     return root
#
# # Функція для додавання ребер до графу та встановлення позицій вузлів для візуалізації
# def add_edges(graph, node, positions, x=0, y=0, layer=1):
#     if node is not None:
#         # Додаємо вузол до графу з його позицією
#         graph.add_node(node.value, pos=(x, y))
#
#         # Якщо існує лівий дочірній вузол, додаємо ребро та встановлюємо позицію
#         if node.left:
#             graph.add_edge(node.value, node.left.value)
#             left_x = x - 1 / layer  # Обчислюємо нову x-позицію для лівого дочірнього вузла
#             add_edges(graph, node.left, positions, x=left_x, y=y - 1, layer=layer + 1)
#
#         # Якщо існує правий дочірній вузол, додаємо ребро та встановлюємо позицію
#         if node.right:
#             graph.add_edge(node.value, node.right.value)
#             right_x = x + 1 / layer  # Обчислюємо нову x-позицію для правого дочірнього вузла
#             add_edges(graph, node.right, positions, x=right_x, y=y - 1, layer=layer + 1)
#
# # Функція для побудови бінарного дерева
# def plot_tree(root):
#     graph = nx.DiGraph()  # Створюємо направлений граф
#     positions = {}  # Словник для збереження позицій вузлів
#     add_edges(graph, root, positions)  # Додаємо вузли та ребра до графу
#     positions = nx.get_node_attributes(graph, 'pos')  # Отримуємо позиції вузлів
#     labels = {node: node for node in graph.nodes()}  # Створюємо мітки для вузлів
#
#     # Малюємо граф
#     nx.draw(graph, positions, with_labels=True, labels=labels, node_size=2000,
#             node_color='skyblue', font_size=16, font_weight='bold', arrows=False)
#     plt.title('Binary Tree Visualization')  # Встановлюємо заголовок графіку
#     plt.show()  # Відображаємо графік
#
# # Приклад використання
# arr = [1, 8, 3, 9, 5, 6, 7]  # Масив, що представляє бінарне дерево
# n = len(arr)  # Кількість елементів у масиві
# root = insert_level_order(arr, None, 0, n)  # Вставляємо вузли у бінарне дерево
#
# # Візуалізуємо бінарне дерево
# plot_tree(root)

print("binarytree")
from binarytree import tree, bst, heap

# Генерація випадкового бінарного дерева та повернення його кореневого вузла.
my_tree = tree(height=3, is_perfect=False)  # Створюємо бінарне дерево висотою 3, яке може бути неповним
print(my_tree)  # Виводимо згенероване бінарне дерево

# Генерація випадкового бінарного дерева пошуку (BST) та повернення його кореневого вузла.
my_bst = bst(height=3, is_perfect=True)  # Створюємо бінарне дерево пошуку висотою 3, яке буде повним
print(my_bst)  # Виводимо згенероване бінарне дерево пошуку

# Генерація випадкової максимальної купи (max heap) та повернення її кореневого вузла.
my_heap = heap(height=3, is_max=True, is_perfect=False)  # Створюємо максимальну купу висотою 3, яка може бути неповною
print(my_heap)  # Виводимо згенеровану максимальну купу





