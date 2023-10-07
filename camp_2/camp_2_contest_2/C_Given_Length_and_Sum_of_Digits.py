from itertools import combinations


_length, _sum = map(int, input().split())


# start_num = 10 ** (_length - 1)
upper_bound =  (_sum // 9)
lower_bound = (_sum // 1)

print(upper_bound)
candidates = [num for num in range(10 ** _length, 10 ** upper_bound)]

all_pairs =  [pair for pair in combinations(candidates, 2) if sum(pair) == _sum]

# find min

minimum = float('inf')
maximum = float('-inf')
for pair in all_pairs:
    first, second = pair
    first_str, second_str = str(first), str(second)
    if (len(first_str) + len(second_str)) <= _length:
        comb = first_str + second_str
        #find min
        to_min = ''.join(sorted(comb))
        #remove leading zeros
        to_min = str(int(to_min))
        to_min = to_min + ('0' * (_length - len(to_min)))

        #find max
        to_max = ''.join(sorted(comb, reverse= True))
        to_max = to_max + ('0' * (_length - len(to_max)))

        minimum = min(minimum, int(to_min))
        maximum = max(maximum, int(to_max))


if minimum == float('inf') or maximum == float('-inf'):
    print(-1, -1)
else:
    print(minimum, maximum)
