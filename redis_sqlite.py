from timeit import timeit
import redis
import sqlite3

setup1 = """
"""

stmt1 = """
if True:
    pass
"""

setup2 = """
"""

stmt2 = """
if False:
    pass
"""

print('hit condition: ', timeit(stmt1, setup=setup1))

print('normal       : ', timeit(stmt2, setup=setup2))

