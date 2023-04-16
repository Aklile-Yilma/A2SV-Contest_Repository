import sys, threading


def main():
    
    n = int(input())
    queenx, queeny = list(map(int, input().split()))
    kingx, kingy = list(map(int, input().split()))
    targetx, targety = list(map(int, input().split()))

    def inbound(row, col):
        return 1 <= row <= n and 1 <= col <= n

    def inCheck(row, col):
        if (row == queenx) or (col == queeny) or ((row + col) == (queenx + queeny)) or ((row - col) == (queenx - queeny)):
            return False
        return True
        

    directions = [(1, 0), (0,1), (-1, 0), (0,-1), (1,1),(-1,-1), (1,-1), (-1,1)]
    visited = set()
    
    def dfs(row, col):
        #basecase
        # print(row, col)
        if row == targetx and col == targety:
            return True
                
        visited.add((row, col))
        
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change
            
            if inbound(new_row, new_col) and (new_row, new_col) not in visited and inCheck(new_row, new_col):
                if dfs(new_row, new_col):
                    return True
                
        
        return False
    
    
    if dfs(kingx, kingy):
        print("YES")
    else:
        print("NO")
        
    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

    


