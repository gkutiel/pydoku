from pytest import fixture
from pyduko.main import Sudoku, get_borders

# template = [
#     ['a', 'a', 'b', 'b'],
#     ['a', 'a', 'b', 'b'],
#     ['c', 'c', 'd', 'd'],
#     ['c', 'c', 'd', 'd']]

template = [
    ['a', 'a', 'c'],
    ['a', 'c', 'b'],
    ['c', 'b', 'b']]

sol = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2]]


part = [
    [0, 0, 1],
    [3, 2, 0],
    [0, 0, 0]]


@fixture
def sudoku():
    return Sudoku(template)


def test_options(sudoku):
    sudoku.sol = sol
    s = sudoku.options()
    assert s[(0, 0)] == {2}, s
    assert s[(0, 1)] == {3}, s


def test_options_part(sudoku):
    sudoku.sol = part
    s = sudoku.options()
    assert s[(0, 0)] == {2}, s
    assert s[(0, 1)] == set(), s
    assert s[(0, 2)] == {1}, s


def test_is_done(sudoku):
    sudoku.sol = sol
    assert sudoku.is_done()

    sudoku.sol = part
    assert not sudoku.is_done()


def test_solve(sudoku):
    sudoku.sol = sol
    assert sudoku.solve()
    assert sudoku.sol == sol

    sudoku.sol = part
    assert not sudoku.solve()

    sudoku.sol = [
        [0, 3, 1],
        [0, 0, 3],
        [0, 0, 2]]

    assert sudoku.solve()
    assert sudoku.sol == [
        [2, 3, 1],
        [1, 2, 3],
        [3, 1, 2]]


def test_get_borders():
    bs = get_borders([
        ['a', 'b'],
        ['a', 'b']])

    assert bs == [(1, 0, 1, 1), (1, 1, 1, 2)], bs

    bs = get_borders([
        ['a', 'b'],
        ['c', 'd']])

    assert bs == [
        (1, 0, 1, 1),
        (0, 1, 1, 1),
        (1, 1, 2, 1),
        (1, 1, 1, 2)], bs


def test_used(sudoku):
    sudoku.sol = [
        [1, 0, 2],
        [0, 0, 0],
        [0, 0, 0]]

    rows, cols, blks = sudoku.used()
    assert rows[0] == {1, 2}, rows
    assert cols[0] == {1}, cols
    assert blks == {'a': {1}, 'c': {2}}, blks


def test_options(sudoku):
    sudoku.sol = [
        [1, 0, 2],
        [0, 0, 0],
        [0, 0, 0]]

    options = sudoku.options()
    assert options[(0, 0)] == {1}, options
    assert options[(0, 1)] == {3}, options
    assert options[(1, 1)] == {1, 3}, options
