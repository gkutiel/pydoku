from email import generator
import random
from pyduko.solver import Solver
from pyduko.templates import templates
from pprint import pprint
from collections import defaultdict
from random import shuffle
from tqdm import tqdm
from math import factorial

from test.test_solver import solver


class Generator:
    def __init__(self, solver):
        n = len(solver)
        self.solver = solver

        state = [[0] * n for _ in range(n)]
        self.state = state
        self.solver.set_state(self.state)

    def mult_ops(self):
        for k, ops in self.solver.options.items():
            if len(ops) > 1:
                yield k, list(ops)

    def fill(self):
        if self.solver.solve():
            return True

        if not self.solver.is_valid():
            return False

        (i, j, b), ops = next(iter(self.mult_ops()))
        random.shuffle(ops)
        self.state[i][j] = ops.pop()
        self.solver.set_state(self.state)
        while not self.fill():
            if not ops:
                self.state[i][j] = 0
                return False

            self.state[i][j] = ops.pop()
            self.solver.set_state(self.state)

        return True

    def generate(self, seed=2022):
        random.seed(seed)
        self.fill()
        assert self.solver.is_done()
        self.state = [
            [list(c)[0] for c in row]
            for row in self.solver.get_solution()]

        n = len(self.solver)
        cells = [(i, j) for i in range(n) for j in range(n)]
        random.shuffle(cells)
        for i, j in cells:
            v = self.state[i][j]
            self.state[i][j] = 0
            self.solver.set_state(self.state)
            if not self.solver.solve():
                self.state[i][j] = v

        return self.state


def get_borders(blks):
    borders = []
    n = len(blks)
    for i in range(n):
        for j in range(n):
            i2, j2 = min(i+1, n-1), min(j+1, n-1)
            if blks[i][j] != blks[i][j2]:
                borders.append((j+1, i, j+1, i+1))
            if blks[i][j] != blks[i2][j]:
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
    blks = templates[6][0]

    solver = Solver(blks)
    generator = Generator(solver)
    state = generator.generate()

    tex(
        blks,
        state,
        'test.tex')
