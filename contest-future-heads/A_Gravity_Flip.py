col = int(input())
blocks = list(map(int, input().split()))

for right in range(col-1, -1, -1):
    for left in range(right - 1, -1, -1):
        
        if blocks[left] > blocks[right]:
            diff = blocks[left] - blocks[right]
            blocks[right] += diff
            blocks[left] -= diff

print(*blocks)

