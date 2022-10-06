import enum
from datetime import datetime

from CNB_application.exceptions import *
from peewee import CharField
from peewee import DateTimeField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import ForeignKeyField

from CNB_application.models.membership import Family

from CNB_application.core import db


class SailingProgramType(str, enum.Enum):
    CATAMARAN = "Catamaran"
    WINDSURF = "Windsurf"
    OPTIMIST = "Optimist"


class SailingProgram(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref="rents")
    date_start = DateTimeField()
    sailing_program = CharField()

    def update_sailing_program(self, program_type: str):
        if program_type in SailingProgramType:
            self.sailing_program = program_type
            self.save()
        else:
            raise InvalidRentingType

    def update_program_date(self, date_start: str):
        try:
            date_start = datetime.strptime(date_start, "%Y-%m-%d")
            self.date_start = date_start
            self.save()
        except (ValueError, TypeError):
            raise InvalidDateFormat

    def get_data(self):
        return self.family, self.sailing_program, self.date_start

    class Meta:
        database = db


with db:
    SailingProgram.create_table(fail_silently=True)
