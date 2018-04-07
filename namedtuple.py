from timeit import timeit

setup1 = """
import collections
test = collections.namedtuple('test', 'cmd, cmd_name')
"""

stmt1 = """
a = test(1, 2)
a.cmd
a.cmd_name
"""

setup2 = """
cmd = 0
cmd_name = 1
"""

stmt2 = """
a = (1, 2)
a[cmd]
a[cmd_name]
"""

setup3 = """
class cc:
    cmd = 0
    cmd_name = 1
"""

stmt3 = """
a = (1, 2)
a[cc.cmd]
a[cc.cmd_name]
"""
print('namedtuple: ', timeit(stmt1, setup=setup1))
print('tuple1     : ', timeit(stmt2, setup=setup2))
print('tuple2     : ', timeit(stmt3, setup=setup3))
