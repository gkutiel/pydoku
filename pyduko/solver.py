from collections import defaultdict


class Solver:
    def __init__(self, blks, state):
        self.n = n = len(blks)

        self.options = {
            (i, j, blks[i][j]): set(range(1, n+1))
            for i in range(n)
            for j in range(n)}

        for i, j, b in self.options.keys():
            v = state[i][j]
            if v != 0:
                self.options[(i, j, b)] = {v}

    def is_done(self):
        return all(len(o) == 1 for o in self.options.values())

    def row(self, r):
        for (i, j, b), ops in self.options.items():
            if i == r:
                yield (i, j, b), ops

    def col(self, c):
        for (i, j, b), ops in self.options.items():
            if j == c:
                yield (i, j, b), ops

    def blk(self, k):
        for (i, j, b), ops in self.options.items():
            if b == k:
                yield (i, j, b), ops

    @staticmethod
    def count_ops(it):
        ops_count = defaultdict(int)
        for _, ops in it:
            ops_count[tuple(ops)] += 1

        return ops_count

    @staticmethod
    def reduceable_ops(ops_count):
        for ops, count in ops_count.items():
            if len(ops) == count:
                yield set(ops)

    @staticmethod
    def other_cells(it, ops):
        for k, v in it:
            if v != ops:
                yield k

    def reduce(self, it):
        it = list(it)
        ops_count = self.count_ops(it)
        for ops in self.reduceable_ops(ops_count):
            for k in self.other_cells(it, ops):
                self.options[k] -= ops

    def reduce_rows(self):
        for i in range(self.n):
            self.reduce(self.row(i))

    def reduce_cols(self):
        for j in range(self.n):
            self.reduce(self.col(j))

    def reduce_blks(self):
        for b in range(self.n):
            self.reduce(self.blk(b))