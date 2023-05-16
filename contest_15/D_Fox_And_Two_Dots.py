row_len, col_len = list(map(int, input().split()))

grid = []
for _ in range(row_len):
    grid.append(list(input()))
    

directions = [1, 0, -1, 0, 1]        
inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
visited = set()
def dfs(row, col, prow, pcol, color):
    
    visited.add((row, col))
    
    for idx in range(len(directions)-1):
        new_row = row + directions[idx]
        new_col = col + directions[idx+1]
        
        cycle = False
        if (new_row, new_col) == (prow, pcol):
            continue
        if (new_row, new_col) in visited:
            return True
        
        if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == color:
            cycle |= dfs(new_row, new_col, row, col)
            
    return cycle

cycle = False
for row in range(row_len):
    for col in range(col_len):
        if (row, col) not in visited:
            if dfs(row, col, -1, -1, grid[row][col]):
                cycle = True
                break
            
if cycle:
    print("YES")
else:
    print("NO")    
            
        
        
        