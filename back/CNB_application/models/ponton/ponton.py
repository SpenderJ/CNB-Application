from datetime import datetime
from typing import Optional

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

    def update_ponton(
        self,
        boat_size: Optional[int],
        date_start: Optional[str],
        date_end: Optional[str],
    ):
        if date_start:
            try:
                date_start = datetime.strptime(date_start, "%Y-%m-%d")
                self.date_start = date_start
            except (ValueError, TypeError):
                raise InvalidDateFormat
        if date_end:
            try:
                date_end = datetime.strptime(date_end, "%Y-%m-%d")
                self.date_end = date_end
            except (ValueError, TypeError):
                raise InvalidDateFormat
        self.boat_size = boat_size if boat_size else self.boat_size
        self.save()

    class Meta:
        database = db


with db:
    Ponton.create_table(fail_silently=True)
