#!/usr/bin/env python3
from utls import get_to_resolve, handle_args, chunk
from itertools import groupby
from typing import Iterable

helpmsg = '''Compact domains to one line(max 9) which have the same ip.
    Usage: like hosts_query.py -h, basically.
    Empty lines, comments and orders won't be kept.'''


def compact(hosts: Iterable[str]):
    lines = (l.split() for l in hosts)
    sortedlines = sorted(lines, key=lambda x: x[0])

    for k, g in groupby(sortedlines, key=lambda x: x[0]):
        for x in chunk(y[1:] for y in g):
            yield k+' '+' '.join(x)


if __name__ == "__main__":
    to_resolve = get_to_resolve(handle_args(helpmsg))
    for line in compact(to_resolve):
        print(line)
