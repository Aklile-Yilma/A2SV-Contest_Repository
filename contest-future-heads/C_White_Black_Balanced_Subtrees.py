from collections import defaultdict
import sys, threading

def main():
    num_testcases = int(input())
    for _ in range(num_testcases):
        nodes = int(input())
        parents = list(map(int, input().split()))
        colors = input()
        
        #imp    
        graph =  defaultdict(list)
        balance = 0

        for child in range(2, nodes+1):
            graph[parents[child-2]].append(child)


        def dfs(root, count):

            nonlocal graph, colors, balance

            if graph[root] == []:
                # [white, black]
                if colors[root-1] == 'W':
                    return [1, 0]
                else:
                    return [0, 1]
            
            for child in graph[root]:
                curr_count = dfs(child, count)
                count =  [count[0]+curr_count[0], count[1] + curr_count[1]]

            #add parent to subtree
            if colors[root-1] == 'W':
                count = [count[0] + 1, count[1]]
            else:
                count = [count[0], count[1] + 1]

            #check balanced
            if count[0] == count[1]:
                balance += 1

            return count

        dfs(1, [0, 0])

        print(balance)


sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()





    

    



