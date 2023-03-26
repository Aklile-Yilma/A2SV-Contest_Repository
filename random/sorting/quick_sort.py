def quick_sort(arr, start, end):
    #base case: empty or len(arr) == 1
    if end - start + 1  <= 1:
        return arr
    
    pivot = arr[start]
    pivot_idx = start
    left = start 
    
    # partition elements smaller than pivot on the left side
    # partition elements greater than pivot on the right side
    for right in range(start, end+1):
        if arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    # move pivot in-between left and right sides

    left -= 1        
    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    
    quick_sort(arr, start, left-1)
    quick_sort(arr, left+1, end)
    return arr

arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
arr2 = [29,10,14,37,14]
 
res = quick_sort(arr, 0, len(arr)-1)
print(res)