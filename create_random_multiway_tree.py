from multiway_node import MultiWayNode

import random


def _create_random_labels(randomizer, num_labels):
    labels = list(range(num_labels))
    randomizer.shuffle(labels)
    return labels


def _create_random_multiway_tree_rec(randomizer, max_children, node_labels):
    node = MultiWayNode(label=node_labels[0])
    remaining_labels = node_labels[1:]
    if remaining_labels:
        num_children = random.randint(1, min(max_children, len(remaining_labels)))
        partition_borders = \
            [0] + \
            sorted(randomizer.sample(range(1, len(remaining_labels)), num_children - 1)) + \
            [len(remaining_labels)]
        for i in range(len(partition_borders) - 1):
            node.add_right_child(
                _create_random_multiway_tree_rec(
                    randomizer=randomizer,
                    max_children=max_children,
                    node_labels=remaining_labels[partition_borders[i]:partition_borders[i + 1]]))
    return node


def create_random_multiway_tree(seed, max_children, num_nodes):
    return _create_random_multiway_tree_rec(
        randomizer=random.Random(seed),
        max_children=max_children,
        node_labels=_create_random_labels(
            randomizer=random.Random(seed + 1),
            num_labels=num_nodes))


if __name__ == '__main__':
    multiway_tree = create_random_multiway_tree(
        seed=42,
        max_children=5,
        num_nodes=100)
    print(multiway_tree)
