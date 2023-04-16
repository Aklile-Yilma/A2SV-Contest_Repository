"""
 understood the problem wrong having odd number of consecutive letters is still correct
"""

num_test_cases = int(input())

for _ in range(num_test_cases):    
    letters = list(input())
    size = len(letters)
    left = 0
    #unique letters
    working_letters = set()
    
    while left < size:
        right = left + 1
        count = 1
        
        while right < size and letters[right] == letters[right-1]:
            count += 1
            right += 1
            left += 1
            
        if count % 2 == 1 and letters[left] not in working_letters:
            working_letters.add(letters[left])

        left += 1
        
    print(''.join(sorted(working_letters)))        
    
"""
previous answer
"""

# num_test_cases = int(input())

# for _ in range(num_test_cases):    
#     letters = list(input())
#     #add padding
#     letters.insert(0, None)
#     letters.append(None)
    
#     #unique letters
#     unique_letters = set(letters)
#     working_letters = []
    
#     for curr_letter in unique_letters:
#         for idx in range(1, len(letters)-1):
#             if letters[idx] == curr_letter:
#                 if letters[idx] != letters[idx-1] and letters[idx] != letters[idx+1]:
#                     working_letters.append(curr_letter)
#                     break
#     working_letters.sort()
#     res = ''.join(working_letters)
#     print(res)        
    
        
    