
from timeit import timeit

setup1 = """
d = {
    1: 1
}
"""

stmt1 = """
d[1]
d[1]
"""

setup2 = """
d = {
    1: 1
}
"""

stmt2 = """
a = d[1]
a
"""

print('get value from dict: ', timeit(stmt1, setup=setup1))
print('use variable       : ', timeit(stmt2, setup=setup2))

