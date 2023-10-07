n = int(input())

# old: set(handles)
handle_map = {}
seen = set()
for _ in range(n):
    old, new = input().split()
    if old not in seen:
        handle_map[old] = [[new, 1]]
        seen.add(old)
        seen.add(new)
    else:
        for key in handle_map:
            for item in handle_map[key]:    
                if old in item:
                    size = len(handle_map[key])
                    handle_map[key].append([new, size + 1])
                    seen.add(new)


print(len(handle_map))
for key in handle_map:
    old = key
    max_size = 0
    new = ''
    for item in handle_map[key]:
        if item[1] > max_size:
            new = item[0]

    print(old, new)




    
