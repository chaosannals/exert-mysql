import aiomysql
import re


class DB:
    '''
    数据库
    '''

    def __init__(self, **config):
        '''
        初始化。
        '''

        self.pool = None
        self.config = config

    async def init(self):
        '''
        数据库初始化。
        '''

        if self.pool == None:
            self.pool = await aiomysql.create_pool(**self.config)
        return self.pool

    async def quit(self):
        '''
        数据库析构。
        '''

        if self.pool != None:
            self.pool.close()
            await self.pool.wait_closed()
            self.pool = None

    async def search(self, sql):
        '''
        搜索获取信息。
        '''

        pool = await self.init()
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchall()

    async def find(self, sql):
        '''
        获取单条数据。
        '''

        pool = await self.init()
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchone()

    async def execute(self, sql):
        '''
        执行 SQL 语句，未提交。
        '''

        pool = await self.init()
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                return await cur.execute(sql)

    async def edit(self, sql):
        '''
        执行 SQL 语句并提交。
        '''

        pool = await self.init()
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
            await conn.commit()

    async def exists_table(self, t):
        '''
        判断表是否存在
        '''

        ts = await self.search(f"SHOW TABLES LIKE '{t}'")
        return ts != None and len(ts) > 0

    async def list_tables(self):
        '''
        列举表
        '''

        ts = await self.search(f'SHOW TABLES')
        return [t[0] for t in ts]

    async def rename_table(self, s, t):
        '''
        重置表名
        '''

        return await self.edit(f'ALTER TABLE `{s}` RENAME TO  `{t}`;')

    async def get_ddl(self, t):
        '''
        获取表 DDL
        '''

        rs = await self.search(f'SHOW CREATE TABLE `{t}`')
        return rs[0][1]

    async def list_columns(self, t):
        '''
        获取表的列信息。
        '''

        rows = await self.search(f'SHOW COLUMNS FROM `{t}`')
        return [{'field': r[0], 'type': r[1], 'null': r[2], 'key': r[3], 'default': r[4], 'extra': r[5]} for r in rows]

    async def has_columns(self, t, fields):
        '''
        查询是否有字段。
        '''

        columns = await self.list_columns(t)
        cs = set([c['field'] for c in columns])
        fs = set(fields)
        ds = fs - cs
        return len(ds) == 0

    async def rename_column(self, t, oc, nc):
        '''
        修改字段名
        '''

        ddl = await self.get_ddl(t)
        pattern = re.compile(f'^\s+`{oc}`\s+(.+?),?\s*$', re.RegexFlag.M)
        m = pattern.search(ddl)
        if m == None:
            raise NameError()
        df = m.group(1)
        return await self.edit(f'ALTER TABLE `{t}` CHANGE COLUMN `{oc}` `{nc}` {df};')

    async def list_indexes(self, t):
        '''
        列举索引。
        '''

        result = {}
        rows = await self.search(f'SHOW INDEX FROM `{t}`')
        for r in rows:
            key = r[2]
            ki = r[3] - 1
            field = r[4]
            if key not in result:
                result[key] = {
                    'fields': []
                }
            while (len(result[key]['fields']) <= ki):
                result[key]['fields'].append(None)
            result[key]['fields'][ki] = field
        return result

    async def add_index(self, t, name, fields):
        '''
        添加索引
        '''

        field_list = '`,`'.join(fields)
        sql = f'''
        ALTER TABLE `{t}`
        ADD INDEX `{name}` (`{field_list}` ASC)
        '''
        await self.edit(sql)
        return sql

    async def new_user(self, user, password):
        '''
        创建用户
        '''

        await self.edit(f'''
            CREATE USER '{user}'@'%'
            IDENTIFIED BY '{password}';
        ''')

    async def grant_all(self, user, schema):
        '''
        赋予用户基本全权限
        '''

        await self.edit(f'''
            GRANT ALL ON {schema}.*
            TO '{user}'@'%';
        ''')

    @staticmethod
    def split_sql(text):
        '''
        切割 SQL
        '''

        string_tag = None
        start = 0
        result = []
        i = 0
        length = len(text)

        while i < length:
            c = text[i]
            if c in ["'", '"']:
                if string_tag == c:
                    if (i + 1) < length:
                        nc = text[i + 1]
                        if string_tag == nc:
                            i += 1
                            continue
                    string_tag = None
                elif string_tag == None:
                    string_tag = c
            # 断句
            if string_tag == None and c == ';':
                result.append(text[start: i])
                start = i + 1
            i += 1
        result.append(text[start:])
        return filter(lambda r: len(r) > 0, [r.strip() for r in result])
