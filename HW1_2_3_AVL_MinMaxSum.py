class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Додавання вузла в дерево
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    # Завдання 1: Знаходження найбільшого значення
    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    # Завдання 2: Знаходження найменшого значення
    def find_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    # Завдання 3: Знаходження суми всіх значень у дереві
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if not node:
            return 0
        return node.data + self._sum_values(node.left) + self._sum_values(node.right)

# Тестування
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(8)
    bst.insert(12)
    bst.insert(17)
    bst.insert(25)

    print("Максимальне значення:", bst.find_max())  # 25
    print("Мінімальне значення:", bst.find_min())   # 8
    print("Сума всіх значень:", bst.sum_values())   # 107
