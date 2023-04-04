import sys
# kth bit from the right, 1 indexed
def kthBitTest(num : int, k : int) -> int:
    # TODO
    num2 = 1 << k
    shifted = num & num2
    
    if shifted > 0:
        return 1   
    return 0

def kthBitTest(num : int, k : int) -> int:
    return (num >> k) & 1


def test():
    assert kthBitTest(6, 2) == 1,'Ooops'
    assert kthBitTest(3, 1) == 1, 'Ooops'
    print('Niceee')

test()