from heapq import heapify, heappop, heappush
num = int(input())

mati_cards = list(map(int, input().split()))
ibsa_cards = list(map(int, input().split()))

heapify(mati_cards)
heapify(ibsa_cards)

mati_max = []
for card in mati_cards:
    heappush(mati_max, -card)

count = 0
while ibsa_cards:
    i_card = heappop(ibsa_cards)
    m_card = heappop(mati_cards)
    if m_card > i_card:
        m_max = -heappop(mati_max)
        heappush(mati_cards, i_card)
        heappush(mati_cards, m_card)
        heappush(ibsa_cards, m_max)
        heappush(mati_max, -i_card)
        count += 1

print(count)
