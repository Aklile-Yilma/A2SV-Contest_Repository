n , m = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))
size = n + m
third_arr = []

first_ptr = 0
second_ptr = 0


while first_ptr < n and second_ptr < m:
    
    if first_arr[first_ptr] <= second_arr[second_ptr]:
        third_arr.append(first_arr[first_ptr])
        first_ptr += 1
    else:
        third_arr.append(second_arr[second_ptr])
        second_ptr += 1


third_arr += first_arr[first_ptr:]
third_arr += second_arr[second_ptr:]

print(*third_arr)  
        
        
        
    