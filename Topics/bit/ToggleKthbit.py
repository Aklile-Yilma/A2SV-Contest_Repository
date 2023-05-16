def toggleBitSet(num : int, k : int) -> int:
	# TODO
    num ^= (1 << k)
    return  num