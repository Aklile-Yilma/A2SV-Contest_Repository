from binarytree import Node
from binarytree import build

values = [3,5,1,6,2,0,8,None,None,7,4]
# values = [1, 2]
root = build(values)


print(root)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        if root == None:
            return None
        
        if root.val == p or root.val == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: 
            return root
        else:
            return left or right
        


s = Solution()
print("answer",s.lowestCommonAncestor(root, 5, 6))



# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         node = [None]
#         def helper(root, p, q, node):
        
#             if root == None:
#                 return False
            
#             if root.val == p or root.val == q:
#                 return True
            
#             if helper(root.left, p, q, node) and helper(root.right, p, q, node):
#                 node[0] = root.val
#                 return True
#         helper(root, p, q, node)    
#         return Node(node[0])