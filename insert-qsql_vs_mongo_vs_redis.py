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

psql_pool = await asyncpg.create_pool(
    **DB_SETTINGS
)

async def insert_test():

    li = []

    for i in range(3000):
        await psql_pool.execute('insert into jackpot_detail values ($1, $2, $3)', 1, 1, 1)

async def insert_test2():

    psql_pool = await asyncpg.create_pool(
        **DB_SETTINGS
    )

    li = []

    for i in range(3000):
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

ac = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://10.0.0.13:27017',
    maxPoolSize=3000
)

tdb = ac['test']

asyncio.get_event_loop().run_until_complete(
    tdb.mgjackpot.drop()
)
asyncio.get_event_loop().run_until_complete(
    tdb.mgjackpot.create_index('jackpot_id', unique=True)
)
asyncio.get_event_loop().run_until_complete(
    tdb.mgdeatil.create_index('jackpot_id')
)

async def insert_test():

    li = []

    for i in range(3000):
        li.append(
            {'jackpot_id': 1, 'node_id': 1, 'cont_seq': 1, 'cont_amt': 1}
        )

    await tdb.jackpot_detail.insert_many(li)

async def insert_test2():
    tdb = ac['test']

    tdb.mgjackpot.insert_one({'jackpot_id': 1, 'cont_list': [], 'cont_amt': 0})

    li = []

    for i in range(3000):
        li.append(
            {'node_id': 1, 'cont_seq': 1, 'cont_amt': 1}
        )

    await tdb.mgjackpot.update({'jackpot_id': 1}, {'$push': {'cont_list': {'$each': li}}})

async def inc_test():
    task_list = []
    tdb.mgjackpot.insert_one({'jackpot_id': 1, 'cont_list': [], 'cont_amt': 0})
    for i in range(3000):
        task_list.append(
            tdb.mgjackpot.update({'jackpot_id': 1}, {'$inc': {'cont_amt': 1}})
        )

    await asyncio.gather(*task_list)


"""

stmt_mongo = """
asyncio.get_event_loop().run_until_complete(insert_test())
"""

stmt_mongo2 = """
asyncio.get_event_loop().run_until_complete(insert_test2())
"""

stmt_mongo_inc = """
asyncio.get_event_loop().run_until_complete(inc_test())
"""

setup_redis = """
import asyncio
import aioredis

REDIS_SETTINGS = {
    # 'address': os.path.join(RUN_DIR, 'redis.sock'),
    'address': ('10.0.0.12', 6379),
    'db': 0,
    'maxsize': 3000,
    # 'minsize': 10,
}
rd_pool = asyncio.get_event_loop().run_until_complete(aioredis.create_pool(
    **REDIS_SETTINGS
))

async def insert_test():

    li = []

    for i in range(3000):
        li.append(
            rd_pool.execute('LPUSH', '1.cont_list', '1.1.1')
        )

    await asyncio.gather(*li)

async def inc_test():
    task_list = []
    for i in range(3000):
        rd_pool.execute('INCRBY', '99.cont_amt', 1)

    await asyncio.gather(*task_list)

"""

stmt_redis = """
asyncio.get_event_loop().run_until_complete(insert_test())
"""
stmt_redis_inc = """
asyncio.get_event_loop().run_until_complete(inc_test())
"""

# print('psql: ', timeit.timeit(stmt_psql, setup_psql, number=1))
print('mongo: ', timeit.timeit(stmt_mongo, setup_mongo, number=1))
print('mongo2: ', timeit.timeit(stmt_mongo2, setup_mongo, number=1))
# print('redis: ', timeit.timeit(stmt_redis, setup_redis, number=1))
# print('mongo_inc: ', timeit.timeit(stmt_mongo_inc, setup_mongo, number=1))
# print('redis_inc: ', timeit.timeit(stmt_redis_inc, setup_redis, number=1))
