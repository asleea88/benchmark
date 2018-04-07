from timeit import timeit

setup1 = """
import redis
r = redis.Redis(unix_socket_path='/home/sangmin/workspace/megajackpot/run/redis.sock')
r.set('a', 1)
"""

stmt1 = """
for i in range(10000):
    var = r.get('a')
"""

setup2 = """
import redis
import multiprocessing
r = redis.Redis(unix_socket_path='/home/sangmin/workspace/megajackpot/run/redis.sock')
r.set('a', 1)

def test():
    for i in range(5000):
        var = r.get('a')
"""

stmt2 = """
p1 = multiprocessing.Process(target=test)
p2 = multiprocessing.Process(target=test)
p1.start()
p2.start()
p1.join()
p2.join()
"""

setup3 = """
import aioredis
import asyncio
import uvloop
LOOP_POLICY = uvloop.EventLoopPolicy()  # None: default
asyncio.set_event_loop_policy(LOOP_POLICY)
loop = asyncio.get_event_loop()

pool = loop.run_until_complete(aioredis.create_pool(
    '/home/sangmin/workspace/megajackpot/run/redis.sock', maxsize=100, minsize=100
    ))

async def test(pool):
#     with await pool as con:
#         a = await con.execute('GET', 'a')
#         a = await con.execute('GET', 'a')
    await pool.execute('GET', 'a')
#     await pool.execute('GET', 'a')

l = []
for i in range(10000):
    l.append(test(pool))
"""

stmt3 = """
loop.run_until_complete(asyncio.gather(*l))
"""
print('redis-get    : ', timeit(stmt1, setup=setup1, number=1))
# print('multip-get   : ', timeit(stmt2, setup=setup2, number=1))
print('uv-aioredis-get : ', timeit(stmt3, setup=setup3, number=1))
