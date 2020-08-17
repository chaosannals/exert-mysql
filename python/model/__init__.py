from peewee import MySQLDatabase, Model, DateTimeField

db = MySQLDatabase(
    'exert',
    user='root',
    password='root',
    host='127.0.0.1',
    port=3306,
)


class BaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def define_index(cls, *args, **argkw):
        index = cls.index(*args, **argkw)
        cls.add_index(index)
