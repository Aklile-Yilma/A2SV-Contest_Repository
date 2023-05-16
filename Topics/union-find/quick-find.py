# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.rep = {i: i for i in range(size)}

    def representative(self, x):
        return self.rep[x]

    def union(self, x, y):
        xrep = self.rep[x]
        yrep = self.rep[y]
        for node in self.rep:
            temp = self.rep[node]
            if temp == yrep:
                self.rep[node] = xrep

    def connected(self, x, y):
        return self.rep[x] == self.rep[y]
