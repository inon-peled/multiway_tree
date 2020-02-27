class BinaryNode:
    def __init__(self, label):
        self._left = None
        self._right = None
        self.label = label

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right
