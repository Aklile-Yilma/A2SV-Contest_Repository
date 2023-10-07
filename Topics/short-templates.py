  
#   inbound function
inbound =  lambda row, col: 0 <= row < row_len and 0 <= col < col_len

# set recursion limit

import sys, threading

def main():
    #your code
    pass


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()
