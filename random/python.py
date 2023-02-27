from typing import *
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = 0
        
        while True:
            
            if fast != slow and nums[fast] == nums[slow]:
                return nums[slow]
            
            if (fast + 2) + 1 >= len(nums):
                print(fast)
                fast = len(nums) % fast
                
            if slow + 1 == len(nums):
                slow = 0
                
            slow += 1
            fast += 2


    
    
s = Solution()
print(s.findDuplicate([1,3,4, 2, 2]))