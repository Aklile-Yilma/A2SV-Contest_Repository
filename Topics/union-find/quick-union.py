# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.rep = [node for node in range(size)]

    def representative(self, x):
        while self.rep[x] != x:
            x = self.rep[x]
        return x

    def union(self, x, y):
        rep1 = self.representative(x)
        rep2 = self.representative(y)
        self.rep[rep2] = rep1

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
