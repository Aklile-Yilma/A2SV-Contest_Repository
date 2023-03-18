size = int(input())
numbers = list(map(int, input().split()))

count_negatives = 0
max_negative = float('-inf')
min_coins = 0
no_zero = True
#count negative numbers:

for num in numbers:
    if num < 0:
        count_negatives += 1
        max_negative = max(max_negative, num)
    if num == 0:
        no_zero = False

#odd amount of negatives    
if count_negatives % 2 != 0 and no_zero:
    #move this max to 1
    min_coins += 1 - (max_negative)
elif count_negatives % 2 != 0 and not no_zero:
    max_negative = float('-inf')
        
for idx in range(len(numbers)):
    curr_num = numbers[idx]
    
    if curr_num == 0:
        min_coins += 1
    elif curr_num > 0:
        #diviation from one
        min_coins += (curr_num - 1) 
    elif curr_num < 0:
        if curr_num == max_negative and count_negatives % 2 != 0:
            count_negatives += 1
            #skip number moved to 1
            continue
        else:
            min_coins += (abs(curr_num) - 1)
            
print(min_coins)
            
        
