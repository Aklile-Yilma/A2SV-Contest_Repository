from collections import Counter
num_test_cases = int(input())

for _ in range(num_test_cases):    
    letters = input()
    unique_letters = set(letters)
    correct_letters = []
    
    for letter in unique_letters:
        left, right = 0, 0
        while right < len(letters):
            if letter == letters[right]:
                if right-left > 1 and letter == letters[left]:
                    correct_letters.append(letters[left])
                    break
                left = right
            right += 1
        
        #check if letter is unique
        freq = Counter(letters)
        if freq[letter] == 1:
            correct_letters.append(letters[left])    
    print(''.join(sorted(correct_letters)))
            
    
    
        
    