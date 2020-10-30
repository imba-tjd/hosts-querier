import sys
from typing import Iterable


def handle_args(helpmsg: str):
    '''handle -h and where to read'''
    for arg in sys.argv:
        if arg[0] == '-':
            if len(arg) == 2 and arg[1] == 'h':
                print(helpmsg)
            else:
                print('Unknown Flag.')
            sys.exit()
    return sys.argv[1:]


def get_input(domains: list[str]):
    '''get domains from args or stdin'''
    return (l.strip() for l in (domains if domains else sys.stdin))


def filter_comments(lst: Iterable[str]):
    '''remove empty lines and comments'''
    return (l if (hashndx := l.find('#')) == -1 else l[:hashndx].strip()
            for l in lst
            if l and l[0] != '#')


def get_to_resolve(domains):
    return set(filter_comments(get_input((domains))))


def chunk(seq: list, n=9):
    return (seq[i:i+n] for i in range(0, len(seq), n))
