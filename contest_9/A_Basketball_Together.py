num_players, power_enemy = list(map(int, input().split()))
players =  list(map(int, input().split()))

players.sort()
left, right = 0, len(players) - 1
total = 0
chosen = [players[right]]
win = 0

while left <= right:
    total = chosen[0] * len(chosen) 
    if  total > power_enemy:
        win += 1
        right -= 1
        chosen = [players[right]]
    else:
        chosen.append(players[left])
        left += 1        
        
print(win)



    
        
    