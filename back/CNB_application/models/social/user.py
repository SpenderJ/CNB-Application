from __future__ import annotations

from CNB_application.core import db
from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import TextField


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    password = CharField(null=True)
    picture = TextField(null=True)
    last_login = DateTimeField()
    account_activated = BooleanField(default=False)
    first_login = BooleanField(default=False)
    created_at = DateTimeField()

    def get_identity(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'picture': self.picture,
            'email': self.email,
        }

    def get_data(self):
        identity = self.get_identity()
        identity['name'] = f'{self.first_name} {self.last_name}'
        return identity, self.account_activated, self.first_login

    class Meta:
        database = db


with db:
    User.create_table(fail_silently=True)
