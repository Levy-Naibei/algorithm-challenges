""" 
You are given pointer to the root of the binary search tree and two values  and . 
You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

Python program to find LCA of v1 and v2 using one
traversal of Binary tree

A binary tree node
 """
 
class Node:
 
    # Constructor to create a new tree node
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
 
def lca(root, v1, v2):
    # Base Case
    if root is None:
        return None
 
    # If either v1 or v2 matches with root's info, report
    #  the presence by returning root (Note that if a info is
    #  ancestor of other, then the ancestor info becomes LCA
    if root.info == v1 or root.info == v2:
        return root
 
    # Look for infos in left and right subtrees
    left_lca = lca(root.left, v1, v2)
    right_lca = lca(root.right, v1, v2)
 
    # If both of the above calls return Non-NULL, then one info
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


# constructed tree
#       1
#   2       3
# 4   5   6   7
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4, 5) = ", lca(root, 4, 5).info)
print("LCA(4, 6) = ", lca(root, 4, 6).info)
print("LCA(3, 4) = ", lca(root, 3, 4).info)
print("LCA(2, 4) = ", lca(root, 2, 4).info)
