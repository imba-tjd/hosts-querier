import sys
from typing import Union, Iterable, List


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


def get_input(file: Union[None, str]):
    '''read from stdin or file'''
    if file is not None:
        with open(file, "r", encoding='utf8') as f:
            return (l.strip() for l in f.readlines())
    else:
        return (l.strip() for l in sys.stdin.readlines())


def filter_comments(lst: Iterable[str]):
    '''remove empty lines and comments'''
    return (l if (hashi := l.find('#')) == -1 else l[:hashi].strip()
            for l in lst
            if l != '' and l[0] != '#')


def get_to_resolve(file: Union[None, str]):
    return set(filter_comments(get_input((file))))


def chunk(seq: Union[List, Iterable[List]], n=9):
    if isinstance(seq, List):
        return [seq[i:i+n] for i in range(0, len(seq), n)]
    else:
        lst = []
        for x in seq:
            lst += x
        return chunk(lst)


if __name__ == "__main__":
    to_resolve = ['asdf', '', '#1234', 'qwer#zxcv']
    resoved = list(filter_comments(to_resolve))
    assert(resoved[0] == 'asdf')
    assert(resoved[1] == 'qwer')
    assert(len(resoved) == 2)
