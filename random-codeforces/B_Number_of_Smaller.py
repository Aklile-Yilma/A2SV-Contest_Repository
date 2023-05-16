n, m = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

smaller_counts = []

first_ptr = 0
for second_ptr in range(len(second_arr)):
    
    while first_ptr < n and first_arr[first_ptr] < second_arr[second_ptr]:
        first_ptr += 1
        
    smaller_counts.append(first_ptr)
    
print(*smaller_counts)

arr = [1, 2, 3, 1]
k = 3
window_size = k
# right = 0

def sliding_window(arr, k):
    left = 0
    
    for right in range(1, len(arr)):
        print(left, right)            
        if abs(right - left) > k:
            left += 1
            
        if arr[right] == arr[left]:
            return True
            
    return False
          
print(sliding_window([1, 2, 3, 1], 3))

        
    

