def sum_tree(node):
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.right.right = TreeNode(40)

print("Сума всіх значень:", sum_tree(root))  # Виведе: Сума всіх значень: 105