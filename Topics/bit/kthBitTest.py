import sys
# kth bit from the right, 1 indexed
def kthBitTest(num : int, k : int) -> int:    
    return ((num) & (1 << (k))) != 0


def test():
    assert kthBitTest(6, 2) == 1,'Ooops'
    assert kthBitTest(3, 1) == 1, 'Ooops'
    print('Niceee')

test()