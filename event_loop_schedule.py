from timeit import timeit


setup1 = """
import asyncio

async def add(a, b):
    return a + b

async def sched(loop):
    for i in range(100000):
        await loop.create_task(add(1,1))

loop = asyncio.get_event_loop()
"""

stmt1 = """
loop.run_until_complete(sched(loop))
"""

setup2 = """
def add(a ,b):
    return a + b
"""

stmt2 = """
for i in range(100000):
    add(1, 1)
"""

setup3 = """
import asyncio
import uvloop

async def add(a, b):
    return a + b

async def sched(loop):
    for i in range(100000):
        await loop.create_task(add(1,1))

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
"""

stmt3 = """
loop.run_until_complete(sched(loop))
"""
print('event loop: ', timeit(stmt1, setup=setup1, number=1))
print('normal    : ', timeit(stmt2, setup=setup2, number=1))
print('uv loop   : ', timeit(stmt3, setup=setup3, number=1))






