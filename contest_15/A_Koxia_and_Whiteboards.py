import heapq
num_test_cases = int(input())

for _ in range(num_test_cases):
    n, m = list(map(int, input().split()))
    whiteboards = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    #sort
    heapq.heapify(whiteboards)
    
    for idx in range(m):
        heapq.heappop(whiteboards)
        heapq.heappush(whiteboards, numbers[idx])
        
        
    print(sum(whiteboards))
    