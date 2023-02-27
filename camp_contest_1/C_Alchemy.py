n = int(input())
ingredients = list(map(int, input().split()))
alphonso =  0
edward = 0
total = sum(ingredients)
curr_sum = 0
left, right = 0, len(ingredients)-1

while curr_sum <= total and left != right:    
    ingredients[left] -= 1
    ingredients[right] -= 1  
    curr_sum += 2

    # print(ingredients, left, right)
    if ingredients[right] == 0 and ingredients[left] == 0 and abs(right - left) == 2: 
        left += 1
        continue
    
    if abs(right - left) == 1:
        continue
        
    if ingredients[left] == 0:
        left += 1
    if ingredients[right] == 0:
        right -= 1
  
edward = left + 1
alphonso = n - left - 1
       
# if curr_sum_left == curr_sum_right:
#     edward += 1

print(edward, alphonso)


