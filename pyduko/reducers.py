from collections import defaultdict


def count_ops(group):
    ops_count = defaultdict(int)
    for _, ops in group:
        ops_count[tuple(ops)] += 1

    return ops_count


def reduceable_ops(ops_count):
    for ops, count in ops_count.items():
        if len(ops) == count:
            yield set(ops)


def reduceable_cells(group, ops):
    for k, v in group:
        if v != ops:
            yield k, v


def reduce(self, it):
    it = list(it)


def reduce_others(group):
    ops_count = count_ops(group)
    for ops in reduceable_ops(ops_count):
        for k, cell_ops in reduceable_cells(group, ops):
            cell_ops -= ops
