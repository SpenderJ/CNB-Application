from __future__ import annotations

import enum
from datetime import datetime

from CNB_application.core import db
from CNB_application.exceptions import InvalidDateFormat
from CNB_application.exceptions import InvalidRentingType
from CNB_application.models.membership import Family
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField


class RentingType(str, enum.Enum):
    HB16 = 'HB16'
    TWIXXY = 'Twixxy'
    DRAGOON = 'Dragoon'
    WINDSURF = 'Windsurf'
    FOIL = 'Foil'
    OPTIMIST = 'Optimist'
    PADDLE = 'Paddle'


class Rent(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref='rents')
    renting_type = CharField()
    date = DateTimeField()
    time_in_minutes = IntegerField()

    def update_rent(
        self,
        renting_type: str | None,
        date: str | None,
        time_in_minutes: str | None,
    ) -> None:
        if renting_type and renting_type in RentingType:
            self.renting_type = renting_type
        else:
            raise InvalidRentingType
        if date:
            try:
                date = datetime.strptime(date, '%Y-%m-%d')  # type: ignore
                self.date = date
            except (ValueError, TypeError):
                raise InvalidDateFormat
        self.time_in_minutes = (
            time_in_minutes if time_in_minutes else self.time_in_minutes
        )
        self.save()

    def get_data(self):
        return self.family, self.renting_type, self.date, self.time_in_minutes

    class Meta:
        database = db


with db:
    Rent.create_table(fail_silently=True)
