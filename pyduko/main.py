import random
from pprint import pprint
from collections import defaultdict
from random import shuffle
from tqdm import tqdm
from math import factorial


class Sudoku:
    def __init__(self, template, seed=2022):
        n = len(template)
        self.bar = tqdm()
        self.it = 1

        self.template = template
        self.sol = [[0] * n for _ in range(n)]
        self.vals = set(range(1, n+1))
        self.cells = [(i, j) for i in range(n) for j in range(n)]

        random.seed(seed)

    def used(self):
        rows = defaultdict(set)
        cols = defaultdict(set)
        blks = defaultdict(set)

        for i, j in self.cells:
            v = self.sol[i][j]
            b = self.template[i][j]

            if v == 0:
                continue

            assert v not in rows[i] and v not in cols[j] and v not in blks[b]

            rows[i].add(v)
            cols[j].add(v)
            blks[b].add(v)

        return rows, cols, blks

    def options(self):
        rows, cols, blks = self.used()

        options = defaultdict(set)
        for i, j in self.cells:
            v = self.sol[i][j]
            b = self.template[i][j]
            if v != 0:
                options[(i, j)] = {v}
            else:
                options[(i, j)] = self.vals - rows[i] - cols[j] - blks[b]

        return options

    def count(self):
        return sum(
            1 if self.sol[i][j] != 0
            else 0
            for i, j in self.cells)

    def solve(self):
        if not self.has_options():
            return False

        if self.is_done():
            return True

        self.it += 1
        self.bar.update(self.it)
        self.bar.set_description(f"{self.count()}/{len(self.cells)}")
        options = self.options()

        for i, j in self.cells:
            if self.sol[i][j] == 0:
                vs = list(options[(i, j)])
                shuffle(vs)
                self.sol[i][j] = vs.pop()
                while not self.solve():
                    self.sol[i][j] = 0
                    if not vs:
                        return False

                    self.sol[i][j] = vs.pop()
                return True

        assert False, 'should not reach here'

    def hide(self):
        cells = self.cells.copy()
        shuffle(cells)
        for i, j in cells:
            v = self.sol[i][j]
            self.sol[i][j] = 0
            if any(len(vs) > 1 for vs in self.options().values()):
                self.sol[i][j] = v

    def has_options(self):
        return all(self.options().values())

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
    n = len(sol)
    borders = get_borders(template)
    with open(out, 'w') as f:
        print(r'''\documentclass{article}
        \usepackage{tikz}
        \usetikzlibrary{patterns}
        \begin{document}
        \begin{center}
        \scalebox{2}{
        \begin{tikzpicture}[x=1cm, y=-1cm]''', file=f)

        print(f'\\draw[] (0,0) grid ({n},{n});', file=f)

        for i in range(n):
            for j in range(n):
                v = sol[i][j]
                if v != 0:
                    print(f'\\node at ({j+.5},{i+.5}) {{{v}}};', file=f)

        for i, j, i2, j2 in borders:
            print(f'%{i, j, i2, j2}', file=f)
            print(f'\\draw[very thick] ({i},{j}) -- ({i2}, {j2});', file=f)

        print(r'''\end{tikzpicture}}
        \end{center}
        \end{document}
        \end{tikzpicture}
        \end{center}
        \end{document}''', file=f)


if __name__ == '__main__':
    template_3x3 = [
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c']]

    # template_4x4 = [
    #     ['a', 'e', 'f', 'b'],
    #     ['a', 'a', 'b', 'b'],
    #     ['a', 'e', 'f', 'b'],
    #     ['e', 'e', 'f', 'f']]

    template_4x4 = [
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd']]

    template_5x5 = [
        ['a', 'd', 'd', 'd', 'd'],
        ['a', 'd', 'e', 'c', 'c'],
        ['a', 'e', 'e', 'e', 'c'],
        ['a', 'a', 'e', 'b', 'c'],
        ['b', 'b', 'b', 'b', 'c']]

    # template_5x5 = [
    #     ['a', 'b', 'c', 'd', 'e'],
    #     ['a', 'b', 'c', 'd', 'e'],
    #     ['a', 'b', 'c', 'd', 'e'],
    #     ['a', 'b', 'c', 'd', 'e'],
    #     ['a', 'b', 'c', 'd', 'e']]

    # template_6x6 = [
    #     ['a', 'a', 'a', 'b', 'b', 'b'],
    #     ['a', 'a', 'a', 'b', 'b', 'b'],
    #     ['c', 'c', 'c', 'd', 'd', 'd'],
    #     ['c', 'c', 'c', 'd', 'd', 'd'],
    #     ['e', 'e', 'e', 'f', 'f', 'f'],
    #     ['e', 'e', 'e', 'f', 'f', 'f']]

    template_6x6 = [
        ['a', 'a', 'a', 'b', 'b', 'b'],
        ['a', 'a', 'e', 'f', 'b', 'b'],
        ['a', 'e', 'e', 'f', 'f', 'b'],
        ['d', 'e', 'e', 'f', 'f', 'c'],
        ['d', 'd', 'e', 'f', 'c', 'c'],
        ['d', 'd', 'd', 'c', 'c', 'c']]

    template_7x7 = [
        ['a', 'a', 'a', 'a', 'b', 'b', 'b'],
        ['a', 'a', 'e', 'e', 'e', 'b', 'b'],
        ['a', 'e', 'e', 'e', 'e', 'f', 'b'],
        ['d', 'g', 'g', 'f', 'f', 'f', 'b'],
        ['d', 'g', 'g', 'g', 'f', 'f', 'c'],
        ['d', 'd', 'g', 'g', 'f', 'c', 'c'],
        ['d', 'd', 'd', 'c', 'c', 'c', 'c']]

    template_8x8 = [
        ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
        ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
        ['c', 'c', 'c', 'c', 'd', 'd', 'd', 'd'],
        ['c', 'c', 'c', 'c', 'd', 'd', 'd', 'd'],
        ['e', 'e', 'e', 'e', 'f', 'f', 'f', 'f'],
        ['e', 'e', 'e', 'e', 'f', 'f', 'f', 'f'],
        ['g', 'g', 'g', 'g', 'h', 'h', 'h', 'h'],
        ['g', 'g', 'g', 'g', 'h', 'h', 'h', 'h']]

    template_9x9 = [
        ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
        ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
        ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
        ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
        ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
        ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
        ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
        ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
        ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i']]

    sudoku = Sudoku(template_5x5, seed=2)
    assert sudoku.solve()
    print()
    pprint(sudoku.sol)
    sudoku.hide()

    tex(
        sudoku.template,
        sudoku.sol,
        'tmp.tex')
