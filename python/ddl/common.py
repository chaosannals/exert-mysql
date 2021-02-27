import aiomysql


class SQL:
    '''
    '''

    def __init__(self, **kws):
        '''
        '''

        self.pool = None
        self.config = {
            'host': kws.get('host', '127.0.0.1'),
            'port': kws.get('port', 3306),
            'user': kws.get('user', 'root'),
            'password': kws.get('password', 'password'),
            'loop': kws.get('loop', None),
            'db': kws.get('db', 'exert')
        }

    async def init(self):
        '''
        初始化。
        '''

        self.pool = await aiomysql.create_pool(**self.config)

    async def quit(self):
        '''
        退出。
        '''

        self.pool.close()
        await self.pool.wait_closed()

    async def search(self, sql):
        '''
        '''
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchall()

    async def get_create_table(self, name):
        '''
        '''

        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f'SHOW CREATE TABLE {name}')
                r = await cur.fetchone()
                return r[1]
