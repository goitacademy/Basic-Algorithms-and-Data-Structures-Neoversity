# двійкове дерево пошуку
from visual_tree import animate_traversal_avl
class Node(object):  # Вузли в дереві
    def __init__(self, data):
        self.data = data  # Вхідні дані
        self.left_child = None  # Лівий нащадок
        self.right_child = None  # Правий нащадок


# Операції на двійковому дереві пошуку
class BinarySearchTree(object):
    def __init__(self):
        self.root = None  # Ініціалізувати корінь як пустий

    # ------------------------- Додавання нового вузла до двійкового дерева пошуку ----------------------------
    # Додати елемент до BST
    def insert(self, data):
        if not self.root:  # Якщо корінь пустий, це перший елемент
            print(f'Вузол {data} був вставлений')
            self.root = Node(data)  # Створити новий вузол дерева
        else:
            self.insert_node(data, self.root)  # Якщо корінь існує, додати новий вузол

    # Додати новий вузол
    # Складність O(log N) якщо дерево збалансоване
    def insert_node(self, data, node):
        # Якщо нові дані менші за дані кореня
        if data < node.data:  # Якщо новий елемент менший за дані поточного вузла
            if node.left_child:  # Якщо поточний вузол[A] має лівого нащадка [B], то
                self.insert_node(data, node.left_child)  # Додати новий вузол зліва від [B]
            else:
                print(f'Вузол {data} був вставлений')
                node.left_child = Node(data)  # Якщо немає лівого нащадка у [A], створити новий вузол зліва від нього

        # Якщо нові дані більші за дані кореня
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                print(f'Вузол {data} був вставлений')
                node.right_child = Node(data)

    # -------------------------- Видалення вузла з двоїчного дерева пошуку ---------------------------

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:  # Якщо вузол пустий, повернути вузол
            return node

        # Якщо дані < кореня, пройти через лівого нащадка поки не знайдемо вузол з "даними"
        # Шукати вузол, який хочемо видалити
        if data < node.data:  # Якщо дані вузла, що потрібно видалити, менші за корінь, перейти наліво
            node.left_child = self.remove_node(data, node.left_child)  # Сказати батьківському вузлу, що його лівий нащадок пустий
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)

        # Інакше стоїмо на вузлі, який хочемо видалити
        else:
            # Якщо поточний вузол є листовим, тобто немає лівого і правого нащадка
            if not node.left_child and not node.right_child:
                print('Видалення листового вузла...')
                del node
                return None  # Повернення None повідомляє батьківський вузол, що його лівий або правий нащадок було видалено
            # Якщо вузол для видалення є батьком і має тільки одного нащадка (праворуч)
            # Вузол -> Правий нащадок
            if not node.left_child:
                print('Видалення вузла з одним правим нащадком...')
                temp_node = node.right_child  # Помістити значення правого нащадка у тимчасову змінну
                del node  # Видалити батьківський вузол
                return temp_node  # Повернути тимчасовий вузол. Батько видаленого вузла --> Тимчасовий вузол

            # Якщо вузол для видалення є батьком і має тільки одного нащадка (ліворуч)
            # Вузол -> Лівий нащадок
            elif not node.right_child:
                print('Видалення вузла з одним лівим нащадком...')
                temp_node = node.left_child
                del node
                return temp_node

            # Якщо вузол для видалення є батьківським вузлом з двома нащадками
            print('Видалення вузла з двома нащадками...')
            # Знайти найбільший вузол у лівому піддереві кореня і помістити в тимчасовий вузол
            temp_node = self.get_predecessor(node.left_child)
            # Замінити дані вузла, що потрібно видалити, даними найбільшого вузла
            node.data = temp_node.data
            # Видалити вузол з найбільшим значенням у лівому піддереві до кореня/вузла, що потрібно видалити
            node.left_child = self.remove_node(temp_node.data, node.left_child)
        return node

    # Отримати найбільше значення у лівому піддереві кореня
    # Повернути вузол з найбільшим значенням
    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    # -------------------------- Отримати мінімальне значення у двоїчному дереві пошуку ---------------------------------
    # Отримати мінімальне значення у двоїчному дереві пошуку
    # Ліве найвіддаленіше значення є найменшим значенням
    def get_min_value(self):
        if self.root:  # Якщо дерево не пусте
            return self.get_min(self.root)  # Перейти до функції getMin

    # Пройти до лівого найвіддаленішого вузла (найменше значення)
    def get_min(self, node):  # Почати проходити від кореня
        if node.left_child:  # Якщо лівий нащадок існує, продовжувати йти поки не досягнемо "NONE"
            return self.get_min(node.left_child)
        return node.data  # Коли ми досягнемо None, отримаємо лівий найвіддаленіший вузол і повернемо його дані

    # ---------------------------- Отримати максимальне значення у двоїчному дереві пошуку ----------------------------------
    # Отримати максимальне значення з двоїчного дерева пошуку (найправіше значення)
    def get_max_value(self):
        if self.root:  # Якщо ми на корені, перейти до функції getMax
            return self.get_max(self.root)

    # Пройти до правого найвіддаленішого вузла (максимальне значення)
    def get_max(self, node):
        if node.right_child:  # Якщо правий нащадок існує, пройти до найправішого вузла
            return self.get_max(node.right_child)
        return node.data  # Повернути дані найправішого вузла

    # ------------------------------ Обхід двоїчного дерева пошуку --------------------------------------
    # Пройти через двоїчне дерево пошуку

    def traversal(self, path):
        if self.root:
            self.pre_order_traversal(self.root, path)

    def pre_order_traversal(self, node, path):
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)

    # -------------------- Пошук вузла у двоїчному дереві пошуку -----------------------
    def search(self, data):
        return self.search_node(data, self.root)

    def search_node(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search_node(data, node.leftChild)
        return self.search_node(data, node.rightChild)

    def display(self, traversal_type=None):
        if traversal_type:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path), traversal_type)
        else:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path))


# -------------------- Тестування -----------------------
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)  # Корінь
    bst.insert(13)
    bst.insert(14)
    bst.insert(12)
    bst.insert(5)
    bst.insert(1)
    bst.display()
    bst.remove(10)
    bst.display()
    found_node = bst.search(5)
    if found_node:
        print(f"Вузол з числом {found_node.data} знайдено.")
    else:
        print("Вузол не знайдено.")

