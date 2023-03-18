num_test_cases = int(input())

for _ in range(num_test_cases):
    size = int(input())
    numbers = list(map(int, input().split()))
    
    turn = True 
    left = 0
    right = size - 1
    
    answer = []
    
    while left <= right:
        if turn:
            answer.append(numbers[left])
            left += 1
            turn = False
        else:
            answer.append(numbers[right])
            right -= 1
            turn = True
            
    print(*answer)