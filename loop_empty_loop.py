from timeit import timeit

setup1 = """
a = {1: []}
"""

stmt1 = """
v = a[1]
for i in v:
    pass
"""

setup2 = """
a = {1: []}
"""

stmt2 = """
v = a[1]
"""

print('loop empty list: ', timeit(stmt1, setup=setup1))

print('normal         : ', timeit(stmt2, setup=setup2))
