n , k = map(int, input().split())
numbers = list(map(int, input().split()))

ans = numbers
original = {num for num in numbers}
seen = {num for num in numbers}

for i in range(n):
    for j in range(i + 1, n):
        total = numbers[i] + numbers[j]
        if total <= k and total not in seen:
            seen.add(total)
            ans.append(total)


if k in seen:
    ans.append(0)

to_remove = []
for i in range(len(ans)):
    possible = False
    for j in range(i + 1, len(ans)):
        total = numbers[i] + numbers[j]
        if total == k:
            possible == True
    if not possible and ans[i] in seen:
        to_remove.append(ans[i])


ans = set(ans)
for num in to_remove:
    if num not in original:
        ans.remove(num)

ans = sorted(list(ans))

print(len(ans))
print(*ans)


