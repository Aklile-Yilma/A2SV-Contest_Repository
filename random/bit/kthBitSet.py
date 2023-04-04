import sys
# Set the Kth bit from the right, 1 indexed
def kthBitSet(num : int, k : int) -> int:
	# TODO
    num2 = 1 << k - 1
    num = num | num2
    
    return num
 

def test():
    assert kthBitSet(6, 1) == 7,'Ooops'
    assert kthBitSet(3, 4) == 11, 'Ooops'
    print('Niceee')

test()
