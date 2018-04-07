from timeit import timeit


setup = """
import aioredis
import asyncio
import uvloop
LOOP_POLICY = uvloop.EventLoopPolicy()  # None: default
asyncio.set_event_loop_policy(LOOP_POLICY)
loop = asyncio.get_event_loop()

# pool = loop.run_until_complete(aioredis.create_pool(
#     '/home/sangmin/workspace/megajackpot/run/redis.sock', maxsize=100, minsize=100
#     ))
pool = loop.run_until_complete(aioredis.create_pool(
    'redis://localhost', maxsize=100, minsize=100
    ))
"""

stmt1 = """
async def test(pool):
    with await pool as con:
        a = await con.execute('GET', 'a')
        a = await con.execute('GET', 'a')
        a = await con.execute('GET', 'a')

l = []
for i in range(10000):
    l.append(test(pool))

loop.run_until_complete(asyncio.gather(*l))
"""
stmt2 = """
async def test2(pool):
    await pool.execute('GET', 'a')
    await pool.execute('GET', 'a')
    await pool.execute('GET', 'a')

l = []
for i in range(10000):
    l.append(test2(pool))

loop.run_until_complete(asyncio.gather(*l))
"""

stmt3 = """
async def test3(pool):
    f1 = pool.execute('GET', 'a')
    f2 = pool.execute('GET', 'a')
    f3 = pool.execute('GET', 'a')
    asyncio.gather(f1, f2, f3)

l = []
for i in range(10000):
    l.append(test3(pool))

loop.run_until_complete(asyncio.gather(*l))
"""

print('pool context : ', timeit(stmt1, setup=setup, number=1))
print('pool execute : ', timeit(stmt2, setup=setup, number=1))
print('pool execute : ', timeit(stmt3, setup=setup, number=1))
