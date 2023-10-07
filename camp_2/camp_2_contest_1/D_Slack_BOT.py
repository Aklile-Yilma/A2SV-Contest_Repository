N = int(input())
strings = []
for _ in range(N):
    string = input()
    strings.append(string)

for i in range(N):
    max_similarity = 0
    for j in range(N):
        if i != j:
            similarity = 0
            for k in range(min(len(strings[i]), len(strings[j]))):
                if strings[i][k] == strings[j][k]:
                    similarity += 1
                else:
                    break
            max_similarity = max(max_similarity, similarity)
    print(max_similarity)
