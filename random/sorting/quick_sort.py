

def quick_sort(arr, start, end):
    #base case: empty or len(arr) == 1
    if end - start + 1 <= 1:
        return arr
    
    pivot = arr[start]
    pivot_idx = start
    left = start + 1
    
    # partition elements smaller than pivot on the left side
    # partition elements greater than pivot on the right side
    
    for right in range(start+1, end):
        print(arr,left, right)
        if arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
                        
    # move pivot in-between left and right sides
    print(arr)
    if left > end-1:
        left = end - 1
            
    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    
    print("after pivot swap", arr)
    quick_sort(arr, start, left-1)
    quick_sort(arr, left + 1, end)
    
    return arr

res = quick_sort([6, 2, 4, 1, 3], 0, 5)
print(res)