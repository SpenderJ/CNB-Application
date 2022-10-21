from __future__ import annotations

from datetime import datetime

from CNB_application.core import db
from CNB_application.exceptions import InvalidDateFormat
from CNB_application.models.membership import Family
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField


class Ponton(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref='pontons')
    date_start = DateTimeField()
    date_end = DateTimeField()
    boat_size = IntegerField()

    def get_data(self):
        return self.family, self.date_start, self.date_end, self.boat_size

    def update_ponton(
        self,
        boat_size: int | None,
        date_start: str | None,
        date_end: str | None,
    ) -> None:
        if date_start:
            try:
                date_start = datetime.strptime(date_start, '%Y-%m-%d')  # type: ignore
                self.date_start = date_start
            except (ValueError, TypeError):
                raise InvalidDateFormat
        if date_end:
            try:
                date_end = datetime.strptime(date_end, '%Y-%m-%d')  # type: ignore
                self.date_end = date_end
            except (ValueError, TypeError):
                raise InvalidDateFormat
        self.boat_size = boat_size if boat_size else self.boat_size
        self.save()

    class Meta:
        database = db


with db:
    Ponton.create_table(fail_silently=True)
