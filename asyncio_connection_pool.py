import asyncpg
import asyncio

DB_SETTINGS = {
    'database': 'postgres',
    'user': 'mega',
    'password': 'mega',
    'host': '127.0.0.1',
}

db_pool = None
connection = None


async def sleep_with_pool():
    async with db_pool.acquire() as con:
        await con.execute('select pg_sleep(1)')
        print('done with pool')


async def sleep():
    global connection
    await connection.execute('select pg_sleep(1)')
    print('done')


async def create_pool():
    global db_pool
    db_pool = await asyncpg.create_pool(**DB_SETTINGS)


async def create_con():
    global connection
    connection = await asyncpg.connect(**DB_SETTINGS)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print('Start...')

    loop.run_until_complete(create_pool())
    loop.run_until_complete(create_con())

    coro_list1 = [sleep_with_pool() for i in range(10)]
    loop.run_until_complete(asyncio.gather(
        *coro_list1
    ))

    coro_list2 = [sleep() for i in range(2)]
    loop.run_until_complete(asyncio.gather(
        *coro_list2
    ))

