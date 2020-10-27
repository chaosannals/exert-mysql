from datetime import datetime
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
    # only_events=[ # 只看指定事件
    #     DeleteRowsEvent,
    #     WriteRowsEvent,
    #     UpdateRowsEvent
    # ],
    # ignored_events=[], # 忽略指定事件
    # only_tables=['e_tester'], # 只看指定表
    # ignored_tables=[], # 忽略指定表
    # only_schemas=[], # 只看指定数据库
    # ignored_schemas=[], # 忽略指定数据库
    blocking=False,
    server_id=2,
    resume_stream=True, # 必须为 True 时，log_file log_pos 定位才有效。
    log_file='binlog.000099', # 文件，需要自行记录。RotateEvent 会给出，记得保留。
    log_pos=4, # 定位号，需要自行记录。每个文件都是从4开始，之后的定位是根据数据长短跳动的
    # GTID 由 source_id:transaction_id 组成
    # source_id 为发起事务 MySQL 实例 UUID
    # transaction_id 为事务序号，从 1 开始递增
    # transaction_id 可以用冒号隔开写多个，减号为连续多个
    # c8671405-081c-11e9-a407-ec0d9a495964:1-5:11-18
    # auto_position 会自动过滤掉指定的 gtid 。
    # auto_position='c8671405-081c-11e9-a407-ec0d9a495964:3472692',

    # skip_to_timestamp='2020-10-01', # 过滤指定时间前的日志
)

for binlogevent in stream:
    print(binlogevent.packet.log_pos)
    if isinstance(binlogevent, RotateEvent):
        print(binlogevent.next_binlog)
    elif hasattr(binlogevent, 'rows'):
        ts = datetime.fromtimestamp(binlogevent.timestamp).isoformat()
        print(f'{binlogevent.packet.timestamp} @ {ts}')
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
