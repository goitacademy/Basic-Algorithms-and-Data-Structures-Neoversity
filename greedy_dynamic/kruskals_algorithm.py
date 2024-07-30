class Graph:
    """
    Iніціалізація графа та додавання ребер і вершин:

    __init__: Ініціалізує граф із заданою кількістю вершин.
    add_edge: Додає ребро між двома вершинами з заданою вагою.
    add_vertex_data: Додає назву (дані) до вершини.
    """
    def __init__(self, size):
        # Ініціалізуємо граф із заданою кількістю вершин
        self.size = size
        self.edges = []  # Список для збереження ребер у форматі (вага, вершина u, вершина v)
        self.vertex_data = [''] * size  # Список для збереження назв вершин

    def add_edge(self, u, v, weight):  # O(1)
        # Додаємо ребро з вершини u до вершини v з заданою вагою
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight))  # Додаємо ребро до списку

    def add_vertex_data(self, vertex, data):  # O(1)
        # Додаємо назву (дані) до вершини
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    """
    Функції для роботи з множинами:

    find: Знаходить корінь множини для вершини з урахуванням стиснення шляхів.
    union: Об'єднує дві множини на основі рангу.
    """
    def find(self, parent, i):  # O(log V)
        # Функція знаходить кореневу вершину множини з урахуванням стиснення шляхів
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):  # O(log V)
        # Об'єднує дві множини на основі рангу
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_algorithm(self):  # O(E log E + E log V)
        """
        Алгоритм Крускала (kruskals_algorithm):
        Ініціалізація:
        result: Список для збереження MST.
        i: Лічильник ребер.
        self.edges = sorted(self.edges, key=lambda item: item[2]): Сортуємо ребра за вагою.
        parent, rank: Ініціалізуємо множини для кожної вершини.
        """
        # Реалізація алгоритму Крускала для пошуку MST
        result = []  # Список для збереження MST
        i = 0  # Лічильник ребер

        # Сортуємо ребра за вагою
        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent = []
        rank = []

        # Ініціалізуємо множини для кожної вершини
        for node in range(self.size):
            parent.append(node)  # Кожна вершина є своїм власним батьком
            rank.append(0)  # Початковий ранг усіх вершин 0

        """
        Основний цикл:
        Проходимо по всіх ребрах (while i < len(self.edges)).
        Знаходимо корені множин для вершин u і v.
        Якщо вершини u і v не утворюють цикл, додаємо ребро до MST і об'єднуємо множини.
        """
        while i < len(self.edges):  # Проходимо по всіх ребрах
            u, v, weight = self.edges[i]
            i += 1

            x = self.find(parent, u)  # Знаходимо корінь множини для вершини u
            y = self.find(parent, v)  # Знаходимо корінь множини для вершини v

            # Якщо вершини u і v не утворюють цикл, додаємо ребро до MST
            if x != y:
                result.append((u, v, weight))  # Додаємо ребро до результату
                self.union(parent, rank, x, y)  # Об'єднуємо множини x і y

        # Виводимо результат
        print("Ребро \tВага")
        for u, v, weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")

# Приклад використання графа
g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

# Додаємо ребра до графа
g.add_edge(0, 1, 4)  # A-B,  4
g.add_edge(0, 6, 10)  # A-G, 10
g.add_edge(0, 2, 9)  # A-C,  9
g.add_edge(1, 2, 8)  # B-C,  8
g.add_edge(2, 3, 5)  # C-D,  5
g.add_edge(2, 4, 2)  # C-E,  2
g.add_edge(2, 6, 7)  # C-G,  7
g.add_edge(3, 4, 3)  # D-E,  3
g.add_edge(3, 5, 7)  # D-F,  7
g.add_edge(4, 6, 6)  # E-G,  6
g.add_edge(5, 6, 11)  # F-G, 11

# Запускаємо алгоритм Крускала для знаходження MST
print("Алгоритм Крускала для знаходження MST:")
g.kruskals_algorithm()
