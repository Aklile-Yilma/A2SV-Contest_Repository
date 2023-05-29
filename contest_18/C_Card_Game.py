rounds = int(input())
mati_cards = list(map(int, input().split()))
ibsa_cards = list(map(int, input().split()))

mati_cards.sort()
ibsa_cards.sort()

half = rounds // 2
ibsa_cards = ibsa_cards[half:]
mati_cards = mati_cards[:half+1]

win = True
for i in range(len(mati_cards)):
    if mati_cards[i] > ibsa_cards[i]:
        win = False
        break

if win:
    print("YES")
else:
    print("NO")
