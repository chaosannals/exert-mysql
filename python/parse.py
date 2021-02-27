import asyncio
from importlib import import_module
ddlc = import_module('ddl.common')
ddlp = import_module('ddl.parser')

async def main(loop):
    lexer = ddlp.CreateTableLexer()
    parser = ddlp.CreateTableParser()
    sql = ddlc.SQL(loop=loop)
    await sql.init()
    ct = await sql.get_create_table('tester')
    parser.parse(lexer.tokenize(ct))
    await sql.quit()
    print(ct)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()