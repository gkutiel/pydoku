from re import template


templates = {
    3: [[['a', 'a', 'b'],
         ['a', 'b', 'b'],
         ['c', 'c', 'c']]],

    4: [[['a', 'b', 'c', 'd'],
         ['a', 'b', 'c', 'd'],
         ['a', 'b', 'c', 'd'],
         ['a', 'b', 'c', 'd']],

        [['a', 'e', 'f', 'b'],
         ['a', 'a', 'b', 'b'],
         ['a', 'e', 'f', 'b'],
         ['e', 'e', 'f', 'f']]],

    5: [[['a', 'd', 'd', 'd', 'd'],
         ['a', 'd', 'e', 'c', 'c'],
         ['a', 'e', 'e', 'e', 'c'],
         ['a', 'a', 'e', 'b', 'c'],
         ['b', 'b', 'b', 'b', 'c']]],

    6: [[['a', 'a', 'a', 'b', 'b', 'b'],
         ['a', 'a', 'a', 'b', 'b', 'b'],
         ['c', 'c', 'c', 'd', 'd', 'd'],
         ['c', 'c', 'c', 'd', 'd', 'd'],
         ['e', 'e', 'e', 'f', 'f', 'f'],
         ['e', 'e', 'e', 'f', 'f', 'f']],

        [['a', 'a', 'a', 'b', 'b', 'b'],
         ['a', 'a', 'e', 'f', 'b', 'b'],
         ['a', 'e', 'e', 'f', 'f', 'b'],
         ['d', 'e', 'e', 'f', 'f', 'c'],
         ['d', 'd', 'e', 'f', 'c', 'c'],
         ['d', 'd', 'd', 'c', 'c', 'c']]],

    7: [[['a', 'a', 'a', 'a', 'b', 'b', 'b'],
         ['a', 'a', 'e', 'e', 'e', 'b', 'b'],
         ['a', 'e', 'e', 'e', 'e', 'f', 'b'],
         ['d', 'g', 'g', 'f', 'f', 'f', 'b'],
         ['d', 'g', 'g', 'g', 'f', 'f', 'c'],
         ['d', 'd', 'g', 'g', 'f', 'c', 'c'],
         ['d', 'd', 'd', 'c', 'c', 'c', 'c']]],

    8: [[['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
         ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
         ['c', 'c', 'c', 'c', 'd', 'd', 'd', 'd'],
         ['c', 'c', 'c', 'c', 'd', 'd', 'd', 'd'],
         ['e', 'e', 'e', 'e', 'f', 'f', 'f', 'f'],
         ['e', 'e', 'e', 'e', 'f', 'f', 'f', 'f'],
         ['g', 'g', 'g', 'g', 'h', 'h', 'h', 'h'],
         ['g', 'g', 'g', 'g', 'h', 'h', 'h', 'h']]],

    9: [[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
         ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
         ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
         ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
         ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
         ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
         ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
         ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
         ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i']]]
}
