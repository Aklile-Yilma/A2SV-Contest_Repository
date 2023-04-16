def mergeSort(left, right, arr):
    
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    
    return merge(left_half, right_half)


def merge(arr1, arr2):
    
    arr1_pointer = 0
    arr2_pointer = 0
    arr3 = []
    idx = 0
    
    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        if arr1[arr1_pointer] <= arr2[arr2_pointer]:
            arr3.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else:
            arr3.append(arr2[arr2_pointer])
            arr2_pointer += 1
        idx += 1
        
    arr3 += arr1[arr1_pointer:]
    arr3 += arr2[arr2_pointer:]
    
    return arr3


def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
    
test()
        