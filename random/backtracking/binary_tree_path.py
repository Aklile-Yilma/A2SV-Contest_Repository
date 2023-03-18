from typing import *
from binarytree import Node
from binarytree import build

class Solution:
    def __init__(self):
        self.paths = []
        
    def binaryTreePaths(self, root) -> List[str]:
        
        
        self.backtrack(root, [])
        
        for idx in range(len(self.paths)):
            path = self.paths[idx]
            self.paths[idx] =  "->".join(path)
        
        return self.paths
        
    def backtrack(self, root, curr_path):
        
        if root.left == None and root.right == None:
            curr_path.append(str(root.val))
            self.paths.append(curr_path.copy())
            return
        
        curr_path.append(str(root.val))
        if root.left:
            self.backtrack(root.left, curr_path)
        elif root.right:
            self.backtrack(root.right, curr_path)
        
        curr_path.pop()
        
        return 
    

values = [1,2,3,None,5]
root = build(values)

s = Solution()
print(s.binaryTreePaths(root))



