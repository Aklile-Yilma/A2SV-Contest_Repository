from collections import defaultdict
n, m = list(map(int, input().split()))
volunteers = []
for _ in range(n):
    volunteers.append(input())

volunteers.sort()

graph = defaultdict(list)
for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

cand = []


def backtrack(start, curr_cand):

    global cand
    if len(cand) < len(curr_cand):
        cand = curr_cand.copy()

    if start == len(volunteers):
        return

    for idx in range(start, len(volunteers)):
        # prune
        curr_person = volunteers[idx]
        exists = False
        for node in graph[curr_person]:
            if node in curr_cand:
                exists = True
                break

        if exists:
            continue
        else:
            curr_cand.append(curr_person)
            backtrack(idx+1, curr_cand)
            curr_cand.pop()

    return


backtrack(0, [])

print(len(cand))
for person in cand:
    print(person)
