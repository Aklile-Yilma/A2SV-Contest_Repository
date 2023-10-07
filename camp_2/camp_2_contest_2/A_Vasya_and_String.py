
n, k = map(int, input().split())
string = input()


def calc(string, k, letter):

    _max = 0
    left = 0
    for right in range(len(string)):
        char = string[right]
        if char == letter:
            _max = max(_max, right - left + 1)
            continue

        if k > 0:
            k -= 1
        else:
            # print("in",left, right, k)
            if string[left] != letter:
                left += 1
                # k += 1
            else:
                while string[left] == letter:
                    left += 1
                left += 1
                # k += 1
            # print("out", right, left, k)
        # print(left, string[left], right, string[right], k)
        _max = max(_max, right - left + 1)

    return _max

ans = max(calc(string, k, 'a'), calc(string, k, 'b'))
# print(calc(string, k, 'b'))
# print(calc(string, k, 'a'))
print(ans)
    

            



