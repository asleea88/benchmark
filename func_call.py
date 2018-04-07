from timeit import timeit

setup1 = """
def a(arg1, arg2, arg3):
    pass
"""

stmt1 = """
a(1,2,3)
"""

setup2 = """
"""

stmt2 = """
pass
"""

print('func    : ', timeit(stmt1, setup=setup1))
print('no func : ', timeit(stmt2, setup=setup2))
