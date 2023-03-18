from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)

print(root)


def preorder(root):
     if root == None:
          return []
      
     return [root.val] + preorder(root.left) +  preorder(root.right)

print("preorder", preorder(root))