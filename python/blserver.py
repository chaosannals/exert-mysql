from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from pymysqlreplication.event import RotateEvent

# pymysql 版本，目前只能用 0.9.0 ，pymysqlreplication 不兼容 0.10.0 。github 已经修复，但是作者没有发布到 pypi.org 上。
mysql_settings = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
}

stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    # only_events=[
    #     DeleteRowsEvent,
    #     WriteRowsEvent,
    #     UpdateRowsEvent
    # ],
    blocking=False,
    server_id=2,
    resume_stream=True,
    log_file='binlog.000063', # 文件，需要自行记录。RotateEvent 会给出，记得保留。
    log_pos=4, # 定位号，需要自行记录。每个文件都是从4开始，之后的定位是根据数据长短跳动的
)

for binlogevent in stream:
    if isinstance(binlogevent, RotateEvent):
        print(binlogevent.next_binlog)
    elif hasattr(binlogevent, 'rows'):
        for row in binlogevent.rows:
            if isinstance(binlogevent, DeleteRowsEvent):
                print(dict(row['values'].items()))
            elif isinstance(binlogevent, UpdateRowsEvent):
                print(dict(row['before_values'].items()))
                print(dict(row['after_values'].items()))
            elif isinstance(binlogevent, WriteRowsEvent):
                print(dict(row['values'].items()))
    else:
        binlogevent.dump()

stream.close()
