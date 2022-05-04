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


def test_status(sudoku):
    sudoku.sol = sol
    s = sudoku.status()
    assert s[(0, 0)] == {2}, s
    assert s[(0, 1)] == {3}, s


def test_status_part(sudoku):
    sudoku.sol = part
    s = sudoku.status()
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

    assert bs == [(0, 0, 0, 1), (1, 0, 1, 1)], bs

    bs = get_borders([
        ['a', 'b'],
        ['c', 'd']])

    assert bs == [
        (0, 0, 0, 1),
        (0, 0, 1, 0),
        (0, 1, 1, 1),
        (1, 0, 1, 1)], bs
