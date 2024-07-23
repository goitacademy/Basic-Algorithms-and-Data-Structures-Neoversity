import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import random
from time import sleep
import warnings
warnings.filterwarnings('ignore')

def build_graph_edges(node, edges=None):
    if edges is None:
        edges = []
    if node:
        if node.left:
            edges.append((node.value, node.left.value))
            build_graph_edges(node.left, edges)
        if node.right:
            edges.append((node.value, node.right.value))
            build_graph_edges(node.right, edges)
    return edges


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def animate_traversal(tree_root, traversal_func, traversal_type):
    path = []
    traversal_func(tree_root, path)
    print(traversal_type, [x.value for x in path])
    G = nx.DiGraph()
    G.add_edges_from(build_graph_edges(tree_root))
    pos = hierarchy_pos(G, root=tree_root.value)

    fig, ax = plt.subplots()

    def update(frame):
        sleep(0.5)
        ax.clear()
        nodes = [node.value for node in path[:frame + 1]]
        nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='lightblue', ax=ax, font_weight='bold')
        nx.draw_networkx_nodes(G, pos=pos, nodelist=nodes, node_color='orange', node_size=2000, ax=ax)
        ax.set_title(f'{traversal_type} Traversal - Step {frame + 1}/{len(path)}')

    ani = FuncAnimation(fig, update, frames=len(path), repeat=True)
    plt.show()


# Visualization functions
def build_graph_edges_avl(node, edges=None):
    if edges is None:
        edges = []
    if node:
        if node.left_child:
            edges.append((node.data, node.left_child.data))
            build_graph_edges_avl(node.left_child, edges)
        if node.right_child:
            edges.append((node.data, node.right_child.data))
            build_graph_edges_avl(node.right_child, edges)
    return edges


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)



def animate_traversal_avl(tree_root, traversal_func, traversal_type=None):
    path = []
    traversal_func(tree_root, path)

    G = nx.DiGraph()
    G.add_edges_from(build_graph_edges_avl(tree_root))
    pos = hierarchy_pos(G, root=tree_root.data)
    fig, ax = plt.subplots()

    def update(frame):
        sleep(0.5)
        ax.clear()
        nodes = [node.data for node in path[:frame + 1]]
        nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='lightblue', ax=ax, font_weight='bold')
        nx.draw_networkx_nodes(G, pos=pos, nodelist=nodes, node_color='orange', node_size=2000, ax=ax)
        ax.set_title(f'{traversal_type} Traversal - Step {frame + 1}/{len(path)}')

    if not traversal_type:
        nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='lightblue', ax=ax, font_weight='bold')
        plt.show()
    else:
        print(traversal_type, [x.data for x in path])
        ani = FuncAnimation(fig, update, frames=len(path), repeat=True)
        plt.show()