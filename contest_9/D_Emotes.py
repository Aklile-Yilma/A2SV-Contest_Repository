num_emotes, max_use, k = list(map(int, input().split()))
emotes = list(map(int, input().split()))


emotes.sort(reverse=True)

first_max = emotes[0]
second_max = emotes[1]

total_first = (max_use % (k+1)) * first_max
total_second =  max_use// (k+1) * (first_max * k + second_max )

max_emotion = total_first + total_second
print(max_emotion) 