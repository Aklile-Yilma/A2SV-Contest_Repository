from collections import deque
def bfs(start, dest, directions, isKing):
    size = 8
    inbound =  lambda row, col: 0 <= row < size and 0 <= col < size
    q = deque()
    q.append((start, (0, 0), 0))
    visited = {start}

    while q:
        node, pre_dir, step = q.popleft()

        if node == dest:
            return step + 1
        
        for dir in directions:
            # print(node[0], dir[0])<<<<<<<<<<<<<<<
            new_row = node[0] + dir[0]
            new_col = node[1] + dir[1]

            if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                if (pre_dir != dir and pre_dir != (0, 0)) and not isKing:
                    step += 1
                if not isKing:
                    q.append(((new_row, new_col), dir, step))
                else:
                    q.append(((new_row, new_col), dir, step + 1))
                    
                visited.add((new_row, new_col))

    return 0

row1, col1, row2, col2 = map(int, input().split())
row1 -= 1
col1 -= 1
row2 -= 1
col2 -= 1
rook = bfs((row1, col1), (row2, col2), [(1, 0), (-1, 0), (0, 1), (0, -1)], False)
bishop = bfs((row1, col1), (row2, col2), [(1, 1), (1, -1), (-1, 1), (-1, -1)], False)
king = bfs((row1, col1), (row2, col2), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], True)

answer = [rook, bishop, king-1]

print(*answer)



