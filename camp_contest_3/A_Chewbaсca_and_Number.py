number = list(input())

for idx in range(len(number)):
    num = int(number[idx])
    if idx == 0 and num == 9:
        continue
    
    if (9 - num) < num:
        number[idx] = str(9 - num) 
        
print(''.join(number))
    

# number_sorted = sorted(set(number))
# first_min = number_sorted[0]
# if first_min == '0':
#     second_min = number_sorted[1]
#     for idx in range(1, len(number)):
#         number[idx] = first_min
#     number[0] = second_min
# else:
#     for idx in range(len(number)):
#         if number[idx] > first_min:
#             number[idx] = first_min

# print(''.join(number))
