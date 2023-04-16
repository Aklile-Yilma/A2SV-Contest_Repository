size, low, high = list(map(int, input().split()))

students = list(map(int, input().split()))
num_subarrays = 0
left = 0
prefix = [0]
for idx in range(size):
    prefix.append(prefix[-1] + students[idx])
    
left = 0
for right in range(1, len(prefix)):
    curr_sum = prefix[right] - prefix[left]
    if low <= curr_sum <= high:
        num_subarrays += 1
    
    while left < right and curr_sum > high:
            left += 1
            curr_sum = prefix[right] - prefix[left]
            if low <= curr_sum <= high:
                num_subarrays += 1
                
# while left < right:
#     left += 1
#     curr_sum = prefix[right] - prefix[left]
#     if low <= curr_sum <= high:
#         num_subarrays += 1
    
print(num_subarrays)
        
    
    
    
    
    