class MultiWayNode:
    def __init__(self, label):
        self._label = label
        self._children = []

    def add_right_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def get_label(self):
        return self._label
