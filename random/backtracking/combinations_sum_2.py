from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #sort
        candidates.sort()
        visited = set()
        print(candidates)
        ans = []
        curr_cand = []
        cand_set = set()
        
        def backtrack(start, curr_cand, total):

            
            if start >= len(candidates) or total > target:
                return
            
            for idx in range(start, len(candidates)):
                
                #prune
                if candidates[idx] not in visited:
                    curr_cand.append(candidates[idx])
                    #check
                    total = sum(curr_cand)
                    if total == target and tuple(curr_cand) not in cand_set:
                        ans.append(curr_cand.copy())
                        cand_set.add(tuple(curr_cand.copy()))
                    if total < target:
                        backtrack(idx + 1 , curr_cand, total)
                        curr_cand.pop()
                    else:
                        if idx == start:
                            curr_cand = []
                            visited.add(candidates[idx])
                            print(visited)
                        break
                    
                    # if len(curr_cand) == 0:
                    #     visited.add(candidates[idx])
                    #     print(visited)
            return 
        
        backtrack(0, curr_cand, 0)
        
        return ans
        
        
        
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))