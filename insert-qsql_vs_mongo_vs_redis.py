import timeit


setup_psql = """
import asyncpg
import asyncio

DB_SETTINGS = {
    'database': 'mega_test',
    'user': 'mega',
    'password': 'mega',
    'host': '10.0.0.11',
    'max_size': 50
}


async def insert_test():

    psql_pool = await asyncpg.create_pool(
        **DB_SETTINGS
    )

    li = []

    for i in range(1000):
        await psql_pool.execute('insert into jackpot_detail values ($1, $2, $3)', 1, 1, 1)

async def insert_test2():

    psql_pool = await asyncpg.create_pool(
        **DB_SETTINGS
    )

    li = []

    for i in range(1000):
        li.append(
            psql_pool.execute('insert into jackpot_detail values ($1, $2, $3)', 1, 1, 1)
        )

    await asyncio.gather(*li)
"""

stmt_psql = """
asyncio.get_event_loop().run_until_complete(insert_test2())
"""


setup_mongo = """
import pymongo
import motor.motor_asyncio
import asyncio

async def insert_test():
    ac = motor.motor_asyncio.AsyncIOMotorClient(
        'mongodb://10.0.0.13:27017',
        maxPoolSize=1000
    )
    tdb = ac['test']

    li = []

    for i in range(1000):
        li.append(
            {'node_id': 1, 'cont_seq': 1, 'cont_amt': 1}
        )

    await tdb.jackpot_detail.insert_many(li)
"""

stmt_mongo = """
asyncio.get_event_loop().run_until_complete(insert_test())
"""

setup_redis = """
import asyncio
import aioredis

async def insert_test():
    REDIS_SETTINGS = {
        # 'address': os.path.join(RUN_DIR, 'redis.sock'),
        'address': ('10.0.0.12', 6379),
        'db': 0,
        'maxsize': 1000,
        # 'minsize': 10,
    }
    rd_pool = await aioredis.create_pool(
        **REDIS_SETTINGS
    )

    li = []

    for i in range(1000):
        li.append(
            rd_pool.execute('LPUSH', '1.cont_list', '1.1.1')
        )

    await asyncio.gather(*li)

"""

stmt_redis = """
asyncio.get_event_loop().run_until_complete(insert_test())
"""


print('psql: ', timeit.timeit(stmt_psql, setup_psql, number=1))
print('mongo: ', timeit.timeit(stmt_mongo, setup_mongo, number=1))
print('redis: ', timeit.timeit(stmt_redis, setup_redis, number=1))
