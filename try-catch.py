import timeit
import time

setup1 = """
"""

stmt1 = """
for _ in range(1000000):
    try:
        pass
    except Exception:
        pass
"""

setup2 = """
"""

stmt2 = """
try:
    for _ in range(1000000):
        pass
except Exception as e:
    pass
"""

setup3 = """
"""

stmt3 = """
for _ in range(1000000):
    pass
"""
print('inner: ', timeit.timeit(stmt1, setup=setup1, number=1))
print('outer: ', timeit.timeit(stmt2, setup=setup2, number=1))
print('no   : ', timeit.timeit(stmt3, setup=setup3, number=1))

