import networkx as nx
import matplotlib.pyplot as plt

# Створення зразкового графу
G = nx.Graph()  # Ініціалізуємо пустий граф

# Додавання вузлів
G.add_nodes_from([1, 2, 3, 4, 5])  # Додаємо вузли до графу

# Додавання ребер
G.add_edges_from([(1, 5), (2, 3), (2, 5), (3, 5)])  # Додаємо ребра між вузлами

# Малювання графу
pos = nx.spring_layout(G)  # Обчислюємо позиції для всіх вузлів для гарного відображення
nx.draw(G, pos, with_labels=True,  # Малюємо граф з позиціями вузлів та мітками
        node_size=700,  # Встановлюємо розмір вузлів
        node_color='skyblue',  # Встановлюємо колір вузлів
        font_size=15,  # Встановлюємо розмір шрифта для міток
        font_color='black',  # Встановлюємо колір шрифта для міток
        font_weight='bold',  # Встановлюємо жирність шрифта для міток
        edge_color='gray')  # Встановлюємо колір ребер

# Відображення графу
plt.title('Network Graph Example')  # Встановлюємо заголовок для графіку
plt.show()  # Відображаємо графік
