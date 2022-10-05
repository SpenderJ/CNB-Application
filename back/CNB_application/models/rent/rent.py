import enum
from datetime import datetime

from peewee import CharField
from peewee import DateTimeField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import ForeignKeyField
from typing import Optional

from CNB_application.models.membership import Family

from CNB_application.exceptions import *
from CNB_application.core import db


class RentingType(str, enum.Enum):
    HB16 = "HB16"
    TWIXXY = "Twixxy"
    DRAGOON = "Dragoon"
    WINDSURF = "Windsurf"
    FOIL = "Foil"
    OPTIMIST = "Optimist"
    PADDLE = "Paddle"


class Rent(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref='rents')
    renting_type = CharField()
    date = DateTimeField()
    time_in_minutes = IntegerField()

    def update_rent(self, renting_type: Optional[str], date: Optional[str], time_in_minutes: Optional[str]):
        if renting_type and renting_type in RentingType:
            self.renting_type = renting_type
        else:
            raise InvalidRentingType
        if date:
            try:
                date = datetime.strptime(date, '%Y-%m-%d')
                self.date = date
            except (ValueError, TypeError):
                raise InvalidDateFormat
        self.time_in_minutes = time_in_minutes if time_in_minutes else self.time_in_minutes
        self.save()

    def get_data(self):
        return self.family, self.renting_type, self.date, self.time_in_minutes

    class Meta:
        database = db


with db:
    Rent.create_table(fail_silently=True)
