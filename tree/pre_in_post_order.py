from visual_tree import animate_traversal

# Binary Tree Node Definition
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def pre_order_traversal(node, path): # Обхід дерева у передпорядку: Корінь -> Ліво -> Право
    if node:
        path.append(node)
        pre_order_traversal(node.left, path)
        pre_order_traversal(node.right, path)


def in_order_traversal(node, path):  # Обхід дерева у порядку: Ліво -> Корінь -> Право
    if node:
        in_order_traversal(node.left, path)
        path.append(node)
        in_order_traversal(node.right, path)


def post_order_traversal(node, path): # Обхід дерева у післяпорядку: Ліво -> Право -> Корінь
    if node:
        post_order_traversal(node.left, path)
        post_order_traversal(node.right, path)
        path.append(node)


# -------------------- Тестування -----------------------
if __name__ == "__main__":
    tree_root = build_sample_tree()

    # Анімований обхід дерева у передпорядку
    animate_traversal(tree_root, pre_order_traversal, 'Pre-Order')

    # Анімований обхід дерева у порядку:
    animate_traversal(tree_root, in_order_traversal, 'In-Order')

    # Анімований обхід дерева у післяпорядку:
    animate_traversal(tree_root, post_order_traversal, 'Post-Order')
