from random import seed
from pyduko.solver import Solver
from pyduko.templates import templates
from pytest import fixture
from pyduko.generator import Generator, get_borders


@fixture
def generator():
    blks = templates[4][0]
    solver = Solver(blks)
    return Generator(solver)


def test_fill(generator):
    assert generator.fill()
    assert generator.solver.is_done()


def test_generate(generator):
    state = generator.generate(seed=2022)
    assert state == [[3, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 2, 4, 0]]
