from collections import defaultdict
def max_depth(tree, root, arr):
    
    if len(tree[root]) == 0:
        return 1
    
    depth = 0
    # print(root, depth)
    for child in tree[root]:
        depth = max(max_depth(tree, child, arr), depth)
        
    return depth + 1
     

n = int(input())
tree = defaultdict(list)

for _ in range(n):
    reposter, _ , poster = input().split()
    parent = poster.lower()
    child = reposter.lower()
    #populate tree
    tree[parent].append(child)

height = max_depth(tree, 'polycarp', [])
print(height)
    
