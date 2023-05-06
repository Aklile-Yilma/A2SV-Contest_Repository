from collections import deque
num_test_cases = int(input())


def bfs(grid, row_len, col_len):
    
    q = deque()
    q.append((0, 0))
    visited = {(0,0)}
    inbound =  lambda row, col: 0 <= row < row_len and 0 <= col < col_len
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1],[1, -1], [-1, -1]]
    
    while q:
        node = q.popleft()
        row, col = node
        
        if (row, col) == (row_len-1, col_len-1):
            return True
        
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change
            
            if (new_row, new_col) not in visited and inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                visited.add((new_row, new_col))
                q.append((new_row, new_col))
                    
    return False    

for _ in range(num_test_cases):
    row_len = 2
    col_len = int(input())
    grid = []
    for _ in range(2):
        grid.append(list(map(int, input())))
        
    if bfs(grid, row_len, col_len):
        print("YES")
    else:
        print("NO")     
    