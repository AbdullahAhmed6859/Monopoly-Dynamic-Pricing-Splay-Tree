class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._splay(self.root, key)
            if key < self.root.key:
                new_node = Node(key)
                new_node.left = self.root.left
                new_node.right = self.root
                self.root.left = None
                self.root = new_node
            elif key > self.root.key:
                new_node = Node(key)
                new_node.right = self.root.right
                new_node.left = self.root
                self.root.right = None
                self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        if self.root is None or self.root.key != key:
            return False
        return True

    def _splay(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            if node.left is None:
                return node
            if key < node.left.key:
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                node.left.right = self._splay(node.left.right, key)
                if node.left.right is not None:
                    node.left = self._rotate_left(node.left)
            if node.left is not None:
                return self._rotate_right(node)
            else:
                return node

        else:
            if node.right is None:
                return node
            if key < node.right.key:
                node.right.left = self._splay(node.right.left, key)
                if node.right.left is not None:
                    node.right = self._rotate_right(node.right)
            elif key > node.right.key:
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            if node.right is not None:
                return self._rotate_left(node)
            else:
                return node

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
