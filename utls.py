import sys
from typing import Iterable, Optional


def handle_args(helpmsg: str):
    '''handle -h and where to read'''
    if len(sys.argv) > 2:
        raise Exception('Too many arguments.')
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == '-h':
            print(helpmsg)
            exit()
        elif arg[0] == '-':
            raise Exception('Unrecognized argument.')
        else:
            return arg


def get_input(file: Optional[str]):
    '''read from stdin or file'''
    if file:
        with open(file, "r", encoding='utf8') as f:
            return (l.strip() for l in f.readlines())
    else:
        return (l.strip() for l in sys.stdin.readlines())


def filter_comments(lst: Iterable[str]):
    '''remove empty lines and comments'''
    return (l if (hashi := l.find('#')) == -1 else l[:hashi].strip()
            for l in lst
            if l != '' and l[0] != '#')


def get_to_resolve(file: Optional[str]):
    return set(filter_comments(get_input((file))))


def chunk(seq: list, n=9):
    return (seq[i:i+n] for i in range(0, len(seq), n))
