from sys import stdin

n = int(stdin.readline().strip())
stack = [[1, 0]]

for _ in range(n):
    command = stdin.readline().strip()

    if command == "add":
        stack[-1][1] += 1
    elif command == "end":
        iterations, add = stack.pop()
        stack[-1][1] += iterations * add
    else:
        _, iterations = command.split()
        stack.append([int(iterations), 0])

if stack[-1][1] > (2**32 - 1):
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])