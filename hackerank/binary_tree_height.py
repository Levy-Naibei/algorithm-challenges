
'''

Calculate the height of binary tree           

// this is a node of the tree , which contains info as data, left , right
'''

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

def height(root):
    if root is None:
        #Height of an empty tree is -1
        return -1
    
    # recursively calculate the height of left and right subtree
    left_height = height(root.left)
    right_height = height(root.right)

    ## Return the maximum height of the left or right subtree, plus 1 for the current node
    return max(left_height, right_height) + 1

# Constructing a simple binary tree
#      1
#     / \
#    2   3
#   / \
#  4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))
