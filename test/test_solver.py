from pytest import fixture
from pyduko.solver import Solver


@fixture
def solver():
    blks = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [2, 2, 3, 3],
        [2, 2, 3, 3]]
    state = [[0] * 4] * 4
    return Solver(blks, state)


def test_count_ops(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(0, 1, 0)] = {1, 2}

    ops_count = solver.count_ops(solver.row(0))

    assert len(ops_count) == 2
    assert ops_count[(1, 2)] == 2
    assert ops_count[(1, 2, 3, 4)] == 2


def test_reduceable_ops(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(0, 1, 0)] = {1, 2}

    ops_count = solver.count_ops(solver.row(0))

    assert list(solver.reduceable_ops(ops_count)) == [{1, 2}]


def test_other_cells(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(0, 1, 0)] = {1, 2}

    other_cells = list(solver.other_cells(solver.row(0), {1, 2}))
    assert other_cells == [(0, 2, 1), (0, 3, 1)]


def test_reduce_rows(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(0, 1, 0)] = {1, 2}

    solver.reduce_rows()

    assert solver.options[(0, 2, 1)] == {3, 4}
    assert solver.options[(0, 3, 1)] == {3, 4}


def test_reduce_cols(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(1, 0, 0)] = {1, 2}

    solver.reduce_cols()

    assert solver.options[(2, 0, 2)] == {3, 4}
    assert solver.options[(3, 0, 2)] == {3, 4}


def test_reduce_blks(solver):
    assert all(o == {1, 2, 3, 4} for o in solver.options.values())

    solver.options[(0, 0, 0)] = {1, 2}
    solver.options[(1, 1, 0)] = {1, 2}

    solver.reduce_blks()

    assert solver.options[(0, 1, 0)] == {3, 4}
    assert solver.options[(1, 0, 0)] == {3, 4}
