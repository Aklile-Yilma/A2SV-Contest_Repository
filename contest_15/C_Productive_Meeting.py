from heapq import *
 
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        nums[i] = [-1 * nums[i], i+1]
    ans = []
 
    heapify(nums)
 
    while len(nums) >= 2:
        # print(nums)
        temp = [0, 0]
        while temp[0] == 0 and len(nums) >= 2:
            temp = heappop(nums)
 
        temp2 = [0, 0]
        while temp2[0] == 0 and len(nums) >= 1:
            temp2 = heappop(nums)
 
        if not temp2[0]:
            temp2[1] = 0
        temp2[0] *= -1
        temp2[0] -= 1
        if temp2[0] > 0:
            temp2[0] *= -1
            heappush(nums, temp2)
 
        temp[0] *= -1
        temp[0] -= 1
        if temp[0] > 0:
            temp[0] *= -1
            heappush(nums, temp)
 
        # print(temp2[0])
        if temp2[1] != temp[1] and temp2[1] != 0:
            ans.append([min(temp2[1], temp[1]), max(temp2[1], temp[1])])
 
    print(len(ans))
    for a in ans:
        print(*a)