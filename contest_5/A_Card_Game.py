size = map(int, input())
cards = list(map(int, input().split()))

left = 0
right = len(cards) - 1
wube_points, henok_points = 0, 0
isWubeTurn = True

while left <= right:
    if cards[left] > cards[right]:
        if isWubeTurn:
            wube_points+= cards[left]
        else:
            henok_points += cards[left]

        left += 1
        
    else:
        if isWubeTurn:
            wube_points += cards[right]
        else:
            henok_points += cards[right]
        
        right -= 1
        
    isWubeTurn = not isWubeTurn
    
        
        
print(wube_points, henok_points)
        
        
    