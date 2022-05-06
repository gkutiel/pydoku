from pprint import pprint

from pyduko.reducers import reduce_others


class Solver:
    def __init__(self, blks, reducers=[
            reduce_others]):

        self.blks = blks
        self.reducers = reducers

    def __len__(self):
        return len(self.blks)

    def set_state(self, state):
        n = len(self)

        self.options = {
            (i, j, self.blks[i][j]): set(range(1, n+1))
            for i in range(n)
            for j in range(n)}

        for i, j, b in self.options.keys():
            v = state[i][j]
            if v != 0:
                self.options[(i, j, b)] = {v}

    def is_done(self):
        return all(len(o) == 1 for o in self.options.values())

    def is_valid(self):
        return all(len(o) >= 1 for o in self.options.values())

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

    def reduce(self):
        for i in range(len(self)):
            for reducer in self.reducers:
                reducer(list(self.row(i)))
                reducer(list(self.col(i)))
                reducer(list(self.blk(i)))

    def solve(self):
        for _ in range(len(self)**2):
            self.reduce()

        return self.is_done()

    def get_solution(self):
        return [
            [o for _, o in self.row(i)]
            for i in range(len(self))]


if __name__ == "__main__":
    blks = [
        [1, 1, 1, 2, 2, 2],
        [1, 1, 1, 2, 2, 2],
        [3, 3, 3, 4, 4, 4],
        [3, 3, 3, 4, 4, 4],
        [5, 5, 5, 6, 6, 6],
        [5, 5, 5, 6, 6, 6]]

    state = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 5, 6, 0, 3],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 3, 0, 5],
        [0, 6, 4, 0, 3, 1],
        [0, 0, 1, 0, 4, 6]]

    solver = Solver(blks)
    solver.set_state(state)
    solver.solve()
    pprint(solver.get_solution())
