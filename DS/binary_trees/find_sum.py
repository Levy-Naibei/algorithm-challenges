class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_sum(root):
    if root is None:
        return 0
    return root.data + find_sum(root.left) + find_sum(root.right)

print(find_sum())