import asyncio
import glob
import os
import aiomysql


class Migrator:
    pool = None

    @classmethod
    async def init(cls, loop):
        '''
        初始化。
        '''

        if cls.pool == None:
            cls.pool = await aiomysql.create_pool(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='password',
                loop=loop
            )

    @classmethod
    async def quit(cls):
        '''
        退出。
        '''

        cls.pool.close()
        await cls.pool.wait_closed()

    @classmethod
    async def search(cls, sql):
        '''
        搜索获取信息。
        '''

        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchall()

    @classmethod
    async def execute(cls, sql):
        '''
        执行 SQL 语句。
        '''

        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                return await cur.execute(sql)

    @classmethod
    async def go_sql_files(cls, folder):
        '''
        列举
        '''

        ps = glob.glob(f'{folder}/*.sql')
        ps.sort()
        for p in ps:
            with open(p, 'r', encoding='utf8') as reader:
                c = reader.read()
                await cls.execute(c)
            print(f'execute: {p}')


async def main(loop):
    '''
    主循环。
    '''

    folder = os.path.dirname(__file__) + '/sql'
    await Migrator.init(loop)
    await Migrator.go_sql_files(folder)
    await Migrator.quit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
