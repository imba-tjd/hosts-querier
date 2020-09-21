from utls import get_to_resolve, handle_args
from itertools import groupby
from typing import Iterable

helpmsg = '''Compact hosts to one line which have the same ip.
    Usage: like hosts_query.py, basically.
    Empty lines, comments and orders won't be kept.'''


def compact(hosts: Iterable[str]):
    line = (l.split(maxsplit=1) for l in hosts)
    sortedline = sorted(line, key=lambda x: x[0])

    for k, g in groupby(sortedline, key=lambda x: x[0]):
        yield k+' '+' '.join(x[1] for x in g)


if __name__ == "__main__":
    to_resolve = get_to_resolve(handle_args(helpmsg))
    for line in compact(to_resolve):
        print(line)
