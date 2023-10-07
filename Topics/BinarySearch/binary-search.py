class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(low, high):
            
            if low > high:
                return -1
            
            mid = (low + high) // 2
            
            if nums[mid] > target:
                return helper(low, mid - 1)
            elif nums[mid] < target:
                return helper(mid + 1, high)
            else:
                return mid
            
        return helper(0, len(nums)-1)
                
