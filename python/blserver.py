from pymysqlreplication import BinLogStreamReader

# pymysql 版本，目前只能用 0.9.0 ，pymysqlreplication 不兼容 0.10.0 。github 已经修复，但是作者没有发布到 pypi.org 上。
mysql_settings = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
}

stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    server_id=100
)

for binlogevent in stream:
    binlogevent.dump()

stream.close()
