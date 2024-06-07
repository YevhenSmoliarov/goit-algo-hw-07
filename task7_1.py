class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.right = TreeNode(40)

print("Найбільше значення:", find_max(root))  # Виведе: Найбільше значення: 40