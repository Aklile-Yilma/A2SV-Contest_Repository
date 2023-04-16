num_recipes, k, num_questions = list(map(int, input().split()))

recipes = []
for idx in range(num_recipes):
    temp = list(map(int, input().split()))
    recipes.append(temp)
    
questions = []
for idx in range(num_questions):
    temp = list(map(int, input().split()))
    questions.append(temp)
    
  
tempretures = [0] * 200002
#create frequency array
for low, high in recipes:
    tempretures[low] += 1
    tempretures[high+1] -= 1 
        
#create prefix array
for idx in range(1, len(tempretures)):
    tempretures[idx] += tempretures[idx-1] 
    
#set valid temp to 1 and invalid to 0        
for idx in range(len(tempretures)):
    temp = tempretures[idx]
    if temp >= k:
        tempretures[idx] = 1
    else:
        tempretures[idx] = 0
        
#create prefix array
for idx in range(1, len(tempretures)):
    tempretures[idx] += tempretures[idx-1] 

#answer each question
for low, high in questions:
    before = tempretures[low - 1]
    admissable = tempretures[high] - before
    print(admissable)
        


            

            
      

    

