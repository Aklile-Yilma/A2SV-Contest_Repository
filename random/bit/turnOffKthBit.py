import sys
# turn off the kth bit from the right, 1 indexed
def turnOffKthBit(num : int, k : int) -> int:
	# TODO
    shifted = 1 << k - 1
    negated = ~ shifted
    num = num & negated
    return num

def turnOffKthBit(num : int, k : int) -> int:
    num &= ~(1 << k)
    return num

def test():
    assert turnOffKthBit(6, 1) == 6,'Ooops'
    assert turnOffKthBit(6, 2) == 4,'Ooops'
    assert turnOffKthBit(3, 4) == 3, 'Ooops'
    print('Niceee')

test()