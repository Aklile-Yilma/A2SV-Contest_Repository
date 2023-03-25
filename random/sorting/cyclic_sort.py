def cyclicsort(nums):
        
    # for ptr in range(len(arr)):
        
    #     while arr[ptr] != ptr + 1:
    #         right = arr[ptr] - 1
    #         arr[ptr], arr[right] = arr[right], arr[ptr]
            
    
    # return arr
    
        #cyclic sort
    for ptr in range(len(nums)):
        curr = nums[ptr]
        while nums[ptr] != ptr + 1:
            print(nums)
            correct_pos = nums[ptr] - 1
            if nums[ptr] == nums[correct_pos]:
                break
            nums[ptr], nums[correct_pos] = nums[correct_pos], nums[ptr] 
            
    return nums

print(cyclicsort([4,3,2,7,8,2,3,1]))