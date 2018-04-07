from timeit import timeit

setup1 = """
l = [1, 2, 3]
l2 = [1]
"""

stmt1 = """

if l2 != []:
    l.extend(l2)


"""

setup2 = """
l = [1, 2, 3]
l2 = []
"""

stmt2 = """
l.extend(l2)
"""

print('hit condition: ', timeit(stmt1, setup=setup1))

print('normal       : ', timeit(stmt2, setup=setup2))

