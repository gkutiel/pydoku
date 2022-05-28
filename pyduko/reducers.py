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


def reduce_others(group):
    ops_count = count_ops(group)
    for ops in reduceable_ops(ops_count):
        for k, cell_ops in reduceable_cells(group, ops):
            cell_ops -= ops


def count_op(group, op):
    return len([g for _, g in group if op in g])


def set_op(group, op):
    for _, ops in group:
        if op in ops:
            ops &= {op}


def reduce_self(group):
    for i in range(len(group)):
        if count_op(group, i) == 1:
            set_op(group, i)
