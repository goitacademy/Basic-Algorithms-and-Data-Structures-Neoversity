class Graph:
    """
    Ініціалізація графа та додавання ребер і вершин:

    __init__: Ініціалізує граф із заданою кількістю вершин, створюючи матрицю суміжності.
    add_edge: Додає ребро між двома вершинами з заданою вагою.
    add_vertex_data: Додає назву (дані) до вершини.
    """
    def __init__(self, size):
        # Ініціалізуємо матрицю суміжності для графа та розмір графа
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  # Зберігаємо назви вершин

    def add_edge(self, u, v, weight):  # O(1)
        # Додаємо ребро між вершинами u і v з заданою вагою
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # Для неорієнтованого графа

    def add_vertex_data(self, vertex, data):  # O(1)
        # Додаємо назву (дані) до вершини
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def prims_algorithm(self):  # O(V^2)
        """
        Алгоритм Пріма (prims_algorithm):

        Ініціалізація:
        in_mst: Вершини, що включені до MST.
        key_values: Ключові значення для вибору мінімальної ваги ребра.
        parents: Масив для збереження MST.

        """
        # Ініціалізуємо структури для зберігання стану MST
        in_mst = [False] * self.size  # Вершини, що включені до MST
        key_values = [float('inf')] * self.size  # Ключові значення для вибору мінімальної ваги ребра
        parents = [-1] * self.size  # Масив для збереження MST

        key_values[0] = 0  # Початкова вершина

        print("Edge \tWeight")
        for _ in range(self.size):  # Повторюємо для всіх вершин
            """
            Основний цикл:
            Знаходимо вершину u з мінімальним ключовим значенням, яка не включена до MST.
            Включаємо вершину u до MST.
            Пропускаємо першу вершину, оскільки вона не має батька.
            Оновлюємо ключове значення для суміжних вершин, якщо ребро має меншу вагу, і оновлюємо батька для вершини.

            """
            # Знаходимо вершину u з мінімальним ключовим значенням, яка не включена до MST
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])

            in_mst[u] = True  # Включаємо вершину u до MST

            if parents[u] != -1:  # Пропускаємо першу вершину, оскільки вона не має батька
                print(f"{self.vertex_data[parents[u]]}-{self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

            for v in range(self.size):  # Перевіряємо всі суміжні вершини
                # Оновлюємо ключове значення для вершини v, якщо ребро (u, v) має меншу вагу
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u  # Оновлюємо батька для вершини v

# Приклад використання графа
g = Graph(8)

# Додаємо назви вершин
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')

# Додаємо ребра до графа з їх вагою
g.add_edge(0, 1, 4)  # A - B
g.add_edge(0, 3, 3)  # A - D
g.add_edge(1, 2, 3)  # B - C
g.add_edge(1, 3, 5)  # B - D
g.add_edge(1, 4, 6)  # B - E
g.add_edge(2, 4, 4)  # C - E
g.add_edge(2, 7, 2)  # C - H
g.add_edge(3, 4, 7)  # D - E
g.add_edge(3, 5, 4)  # D - F
g.add_edge(4, 5, 5)  # E - F
g.add_edge(4, 6, 3)  # E - G
g.add_edge(5, 6, 7)  # F - G
g.add_edge(6, 7, 5)  # G - H

# Запускаємо алгоритм Пріма для знаходження MST
print("Prim's Algorithm MST:")
g.prims_algorithm()
