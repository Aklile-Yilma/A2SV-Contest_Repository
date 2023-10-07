s = input()
l = input()

ptr_s = len(s) - 1
ptr_l = len(l) - 1

common_len = 0
while ptr_s >= 0 and ptr_l >= 0:
    if s[ptr_s] == l[ptr_l]:
        common_len += 2
    else:
        break

    ptr_s -= 1
    ptr_l -= 1

min_moves = (len(s) + len(l)) - common_len

print(min_moves)

