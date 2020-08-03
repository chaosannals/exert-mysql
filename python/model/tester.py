from peewee import CharField
from . import BaseModel, DateTimeField

class Tester(BaseModel):
    jobnumber = CharField(max_length=8)
    name = CharField(max_length=120)
    create_at = DateTimeField(default='CURRENT_TIMESTAMP')
    update_at = DateTimeField(null=True)

Tester.define_index(Tester.jobnumber.asc(), unique=True)
Tester.define_index(Tester.create_at.asc())
Tester.define_index(Tester.update_at.asc())
