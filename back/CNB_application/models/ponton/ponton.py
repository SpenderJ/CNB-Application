from datetime import datetime

from peewee import DateTimeField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import ForeignKeyField

from CNB_application.exceptions import *
from CNB_application.models.membership import Family

from CNB_application.core import db


class Ponton(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref="pontons")
    date_start = DateTimeField()
    date_end = DateTimeField()
    boat_size = IntegerField()

    def get_data(self):
        return self.family, self.date_start, self.date_end, self.boat_size

    def update_ponton_date(self, date_start: str, date_end: str):
        try:
            date_start = datetime.strptime(date_start, "%Y-%m-%d")
            date_end = datetime.strptime(date_end, "%Y-%m-%d")
            self.date_start = date_start
            self.date_end = date_end
            self.save()
        except (ValueError, TypeError):
            raise InvalidDateFormat

    class Meta:
        database = db


with db:
    Ponton.create_table(fail_silently=True)
