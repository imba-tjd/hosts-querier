#!/usr/bin/env python3
from utls import get_to_resolve, handle_args, chunk
from itertools import groupby
from typing import Iterable


def compact(hosts: Iterable[str]):
    '''Compact domains to one line(max 9) which have the same ip.'''
    lines = (l.split() for l in hosts)
    sortedlines = sorted(lines, key=lambda x: x[0])

    for k, g in groupby(sortedlines, key=lambda x: x[0]):
        for x in chunk(sum((y[1:] for y in g), [])):
            yield k+' '+' '.join(x)


if __name__ == "__main__":
    to_resolve = get_to_resolve(handle_args(compact.__doc__))
    for line in compact(to_resolve):
        print(line)
