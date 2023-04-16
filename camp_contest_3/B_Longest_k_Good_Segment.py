n , k = list(map(int, input().split()))
integers = list(map(int, input().split()))

answer = [0, 0]
window_dict = {}
left = 0
for right in range(n):
    num = integers[right]
    
    if num in window_dict:
        window_dict[num] += 1
    else:
        window_dict[num] = 1
        
    while len(window_dict) > k:
        window_dict[integers[left]] -= 1
        if window_dict[integers[left]] == 0:
            del window_dict[integers[left]]
        left += 1        
    
    if (answer[1] - answer[0]) < (right - left):
        answer[0] = left
        answer[1] = right

print(answer[0] + 1, answer[1] + 1)