from collections import defaultdict, deque
n = int(input())
words = []
for _ in range(n):
    words.append(input())

letters = ''


def findOrder(alien_dict, N, k):
    global letters
    # code here
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for curr in range(1, N):
        ltrPtr = 0
        prev = curr-1
        max_size = min(len(alien_dict[prev]), len(alien_dict[curr]))
        while ltrPtr < max_size and alien_dict[prev][ltrPtr] == alien_dict[curr][ltrPtr]:
            ltrPtr += 1

        if ltrPtr < max_size:
            parent = alien_dict[prev][ltrPtr]
            child = alien_dict[curr][ltrPtr]
            graph[parent].append(child)
            indegree[child] += 1
        elif ltrPtr >= max_size and len(alien_dict[prev]) > len(alien_dict[curr]):
            return False

    q = deque()
    # append independent nodes to the q
    for letter in graph:
        # letter = chr(97+idx)
        if indegree[letter] == 0:
            q.append(letter)

    order = []
    while q:
        letter = q.popleft()
        order.append(letter)

        for child in graph[letter]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)

    # if cycle return false
    if len(order) != len(graph.keys()):
        return False

    answer = []
    order_set = set(order)
    # print(order)
    for x in range(ord('a'), ord('z')+1):
        char = chr(x)
        if char not in order_set:
            answer.append(char)
        if char == order[0]:
            answer.append(''.join(order))

    letters = "".join(answer)

    return True


if findOrder(words, n, 26):
    print(letters)
else:
    print("Impossible")
