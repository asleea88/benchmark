from timeit import timeit

setup1 = """
class A:
    def __init__(self, b):
        self.b = b

    @property
    def bb(self):
        return self.b.bb

class B:
    def __init__(self):
        self.bb = 'bb'

a = A(B())
"""

stmt1 = """
a.b.bb
"""

stmt2 = """
a.bb
"""

print('direct  : ', timeit(stmt1, setup=setup1))
print('property: ', timeit(stmt2, setup=setup1))
