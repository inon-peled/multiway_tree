from binary_node import BinaryNode
from create_random_multiway_tree import create_random_multiway_tree


def multiway_to_binary(root):
    binary_root = BinaryNode(label=root.get_label())
    if root.get_children():
        subtrees = [multiway_to_binary(child) for child in root.get_children()]
        _concatenate_right(subtrees)
        binary_root.set_left(subtrees[0])
    return binary_root


def _concatenate_right(nodes):
    for i in range(len(nodes) - 1):
        nodes[i].set_right(nodes[i + 1])


if __name__ == '__main__':
    multiway_tree = create_random_multiway_tree(
        seed=1,
        max_children=3,
        num_nodes=10)
    binary_tree = multiway_to_binary(multiway_tree)
    print(binary_tree)