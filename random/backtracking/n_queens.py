from typing import *
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        result = 0
        valid_queen_pos  = set()
        def backtrack(row):
            
            nonlocal result 
            if row > n:
                if len(valid_queen_pos) == n:
                    result += 1
                return 
            
            for col in range(1, n+1):

                if isValid((row, col), valid_queen_pos):
                    valid_queen_pos.add((row, col))
                    backtrack(row + 1)
                    valid_queen_pos.remove((row, col))
            
            return
        
        def isValid(pos, valid_queen_pos):
            
            row, col = pos
            
            #check upward
            for idx in range(row, 0, -1):
                if (idx, col) in valid_queen_pos:
                    return False
                
            #check right diagonal
            diag_col = col - 1
            for idx in range(row, 0, -1):
                if (idx, diag_col+1) in valid_queen_pos:
                    return False
                
            #check left diagonal
            diag_col = col + 1
            for idx in range(row, 0, -1):
                if (idx, diag_col - 1) in valid_queen_pos:
                    return False
                
            return True

            
        backtrack(1)
        
        return result
        
        
        
        
s = Solution()
s.totalNQueens(4)