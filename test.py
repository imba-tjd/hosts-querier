#!/usr/bin/env python3
from query import resolve
from compact import compact
from utls import filter_comments, chunk

ans = resolve('foo.bar.10.0.0.1.xip.io')
assert ans
assert next(ans) == '10.0.0.1'

chunked = chunk(list(range(10)))
next(chunked)
assert next(chunked)[0] == 9

compacted = compact(['10.0.0.1 a b c d e', '10.0.0.1 f g h i j'])
assert next(compacted) == '10.0.0.1 a b c d e f g h i'
assert next(compacted) == '10.0.0.1 j'

to_resolve = ['asdf', '', '#1234', 'qwer #zxcv']
resoved = list(filter_comments(to_resolve))
assert len(resoved) == 2
assert resoved[0] == 'asdf'
assert resoved[1] == 'qwer'
