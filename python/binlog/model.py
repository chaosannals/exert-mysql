from tortoise.models import Model
from tortoise import fields, Tortoise


async def db_init():
    '''
    '''
    await Tortoise.init(
        db_url='sqlite://binlog.db',
        modules={
            'models': [
                'binlog.model',
            ]
        }
    )


async def db_quit():
    '''
    '''
    await Tortoise.close_connections()


class ReplicationTask(Model):
    class Meta:
        table = 'e_replication_task'

    identity = fields.IntField(pk=True)
    hostname = fields.TextField()
    hostport = fields.IntField()
    username = fields.TextField()
    password = fields.TextField()
    log_filename = fields.TextField()
    log_position = fields.IntField()
    log_gtid = fields.TextField()
