def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)

print("Найменше значення:", find_min(root))  # Виведе: Найменше значення: 5