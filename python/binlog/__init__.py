from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from pymysqlreplication.event import RotateEvent, GtidEvent
from .model import ReplicationTask


class Replicator:
    '''
    迁移器
    '''

    def __init__(self):
        '''
        初始化日志读取器。
        '''

        self.status = status
        self.reader = BinLogStreamReader(
            connection_settings={
                'host': status.hostname,
                'port': status.hostport,
                'user': status.username,
                'passwd': status.password,
            },
            only_events=[
                RotateEvent,
                GtidEvent,
                DeleteRowsEvent,
                WriteRowsEvent,
                UpdateRowsEvent
            ],
            blocking=True,
            server_id=2,
            resume_stream=True,
            log_file=status.log_filename if status.log_filename else None,
            log_pos=status.log_position,
        )

    async def replicate(self):
        '''
        '''

        i = 0
        for be in self.reader:
            if isinstance(be, RotateEvent):
                await ReplicationTask.filter(id=self.status.id).update(log_filename=be.next_binlog)
            elif isinstance(be, GtidEvent):
                await ReplicationTask.filter(id=self.status.id).update(log_gtid=be.gtid)
            print(f'{i} => {be.packet.log_pos}')
            self.status.log_position = be.packet.log_pos
            await ReplicationTask.filter(id=self.status.id).update(log_position=be.packet.log_pos)
            if i > 10000:
                self.reader.close()
                break
            i += 1
