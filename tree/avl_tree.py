# AVL Tree
# Під час кожного додавання перевіряється, чи дерево збалансоване за висотою
# Якщо воно незбалансоване, виконується обертання для балансування

from visual_tree import animate_traversal_avl

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None  # Лівий нащадок поточного вузла
        self.right_child = None  # Правий нащадок поточного вузла
        self.height = 0  # Висота дерева для перевірки балансування


# Виконання операцій на AVL-дереві
class AVL(object):
    def __init__(self):
        self.root = None  # Кореневий вузол

    # --------------------------- Обчислення висоти AVL-дерева ---------------------------------
    def calc_height(self, node):
        if not node:  # Якщо цей вузол нульовий
            return -1  # повертаємо -1; лівий і правий нащадки листових вузлів
        return node.height

    # ------------------------------- Додавання вузла до AVL-дерева ----------------------------
    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:  # Якщо це кореневий вузол, створюємо новий вузол
            print(f'Вузол {data} був вставлений')
            return Node(data)
        if data < node.data:  # Якщо дані менші за поточний вузол, йдемо ліворуч, інакше праворуч
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        # Отримуємо висоту нового вузла
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1

        # Вузол був вставлений. Тепер перевіряємо, чи були порушення AVL-дерева
        return self.settle_violation(data, node)

    # -------------------- Вирішення порушень при додаванні нового вузла --------------------------
    def settle_violation(self, data, node):
        balance = self.calc_balance(node)

        # Випадок 1: Ліва ліва ситуація
        if balance > 1 and data < node.left_child.data:
            print("Ліва ліва ситуація...")
            return self.rotate_right(node)

        # Випадок 2: Права права ситуація
        if balance < -1 and data > node.right_child.data:
            print('Права права ситуація...')
            return self.rotate_left(node)

        # Випадок 3: Ліва права ситуація
        if balance > 1 and data > node.left_child.data:
            print('Ліва права ситуація...')
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        # Випадок 4: Права ліва ситуація
        if balance < -1 and data < node.right_child.data:
            print('Права ліва ситуація...')
            node.right_child = self.rotate_right(node.right_child)  # Тут вузол є кореневим вузлом
            return self.rotate_left(node)

        return node

    # ------------------------------- Перевірка, чи дерево збалансоване -------------------------------
    # Якщо повертає значення > 1, це означає, що дерево лівобічно важке
    # Виконуємо праве обертання для балансування
    # Якщо повертає значення < -1, це означає, що дерево правобічно важке
    # Виконуємо ліве обертання для балансування
    def calc_balance(self, node):
        if not node:
            return 0
        return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    # Праве обертання вузлів для балансування AVL-дерева
    # Часова складність O(1)
    def rotate_right(self, node):
        print('Праве обертання на вузлі ', node.data)  # C <- B <- D -> E; Кореневий вузол - "D"
        temp_left_child = node.left_child  # temp_left_child => B
        t = temp_left_child.right_child  # t = C

        # Праве обертання
        temp_left_child.right_child = node  # "D" стає правим нащадком "B"; B -> D
        node.left_child = t  # "C" стає лівим нащадком "D"

        # Обчислення висоти AVL-дерева
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_left_child.height = max(self.calc_height(temp_left_child.left_child),
                                   self.calc_height(temp_left_child.right_child)) + 1
        return temp_left_child  # Кореневий вузол після обертання

    # Ліве обертання вузлів для балансування AVL-дерева
    # Часова складність O(1)
    def rotate_left(self, node):
        print('Ліве обертання на вузлі ', node.data)
        temp_right_child = node.right_child
        t = temp_right_child.left_child

        # Ліве обертання
        temp_right_child.left_child = node
        node.right_child = t

        # Обчислення висоти AVL-дерева
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_right_child.height = max(self.calc_height(temp_right_child.left_child),
                                    self.calc_height(temp_right_child.right_child)) + 1
        return temp_right_child  # Кореневий вузол після обертання

    # ------------------------------ Видалення вузла з AVL-дерева -----------------------
    # Видалення вузла [Deletion]
    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print('Видалення листового вузла...')
                del node
                return None
            if not node.left_child:
                print('Видалення правого нащадка...')
                tempNode = node.right_child
                del node
                return tempNode
            if not node.right_child:
                print('Видалення лівого нащадка...')
                tempNode = node.left_child
                return tempNode
            print('Видалення вузла з двома нащадками...')
            tempNode = self.get_predecessor(node.left_child)
            node.data = tempNode.data
            node.left_child = self.remove_node(tempNode.data, node.left_child)

        if not node:
            return node

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        balance = self.calc_balance(node)

        # Двічі ліва важка ситуація
        if balance > 1 and self.calc_balance(node.left_child) >= 0:
            return self.rotate_right(node)

        # Двічі права важка ситуація
        if balance < -1 and self.calc_balance(node.right_child) <= 0:
            return self.rotate_left(node)

        # Ліва права ситуація
        if balance > 1 and self.calc_balance(node.left_child) < 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        # Права ліва ситуація
        if balance < -1 and self.calc_balance(node.right_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    # --------------------- Обхід AVL-дерева ------------------
    def traverse(self, path):
        if self.root:
            self.pre_order_traversal(self.root, path)

    def pre_order_traversal(self, node, path):
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)

    # --------------------- Візуалізація AVL-дерева ------------------

    def display(self, traversal_type=None):
        if traversal_type:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path), traversal_type)
        else:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path))


# ------------------- Тестування -----------------
if __name__ == '__main__':
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.display()
    avl.insert(6)
    avl.insert(15)
    avl.display()
    avl.remove(20)
    avl.remove(15)
    avl.display('Pre-Order')
