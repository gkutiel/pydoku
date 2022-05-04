import random
from pprint import pprint
from collections import defaultdict
from random import shuffle


class Sudoku:
    def __init__(self, template, seed=2022):
        n = len(template)

        self.template = template
        self.sol = [[0] * n for _ in range(n)]
        self.vals = set(range(1, n+1))

        random.seed(seed)
        cells = [(i, j) for i in range(n) for j in range(n)]
        shuffle(cells)

        self.cells = cells

    def status(self):
        rows = defaultdict(set)
        cols = defaultdict(set)
        blks = defaultdict(set)

        for i, j in self.cells:
            v = self.sol[i][j]
            b = self.template[i][j]
            if v == 0:
                continue

            rows[i].add(v)
            cols[j].add(v)
            blks[b].add(v)

        status = defaultdict(set)
        for i, j in self.cells:
            v = self.sol[i][j]
            b = self.template[i][j]
            if v != 0:
                status[(i, j)] = {v}
            else:
                status[(i, j)] = self.vals - rows[i] - cols[j] - blks[b]

        return status

    def solve(self):
        if not self.is_valid():
            return False

        if self.is_done():
            return True

        status = self.status()

        for i, j in self.cells:
            vs = status[(i, j)]

            if not vs:
                return False

            if self.sol[i][j] == 0:
                self.sol[i][j] = vs.pop()
                while not self.solve():
                    if not vs:
                        return False
                    self.sol[i][j] = vs.pop()
                return True

        assert False, 'should not reach here'

    def clear(self):
        for i, j in self.cells:
            v = self.sol[i][j]
            self.sol[i][j] = 0
            if any(len(vs) > 1 for vs in self.status().values()):
                self.sol[i][j] = v

    def is_valid(self):
        return all(self.status().values())

    def is_done(self):
        return all(v != 0 for row in self.sol for v in row)


def get_borders(template):
    borders = []
    n = len(template)
    for i in range(n):
        for j in range(n):
            i2, j2 = min(i+1, n-1), min(j+1, n-1)
            if template[i][j] != template[i][j2]:
                borders.append((j+1, i, j+1, i+1))
            if template[i][j] != template[i2][j]:
                borders.append((j, i+1, j+1, i+1))
    return borders


def tex(template, sol, out):
    n = len(template)
    borders = get_borders(template)
    print(len(borders))
    with open(out, 'w') as f:
        print(r'''\documentclass{article}
        \usepackage{tikz}
        \usetikzlibrary{patterns}
        \begin{document}
        \begin{center}
        \begin{tikzpicture}[x=1cm, y=-1cm]''', file=f)

        print(f'\\draw[] (0,0) grid ({n},{n});', file=f)
        for i in range(n):
            for j in range(n):
                print(f'\\node at ({i+.5},{j+.5}) {{{template[j][i]}}};', file=f)
        for i, j, i2, j2 in borders:
            print(f'%{i, j, i2, j2}', file=f)
            print(f'\\draw[very thick, red] ({i},{j}) -- ({i2}, {j2});', file=f)

        print(r'''\end{tikzpicture}
        \end{center}
        \end{document}
        \end{tikzpicture}
        \end{center}
        \end{document}''', file=f)


if __name__ == '__main__':
    template = [
        ['a', 'a', 'a', 'b', 'b', 'b'],
        ['a', 'a', 'a', 'b', 'b', 'b'],
        ['c', 'c', 'c', 'd', 'd', 'd'],
        ['c', 'c', 'c', 'd', 'd', 'd'],
        ['e', 'e', 'e', 'f', 'f', 'f'],
        ['e', 'e', 'e', 'f', 'f', 'f']]

    tex(template, None, 'tmp.tex')
