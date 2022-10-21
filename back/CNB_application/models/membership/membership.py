from __future__ import annotations

import datetime
import enum

from CNB_application.core import db
from CNB_application.exceptions import MembershipTypeNotFound
from CNB_application.exceptions import InvalidDateFormat
from CNB_application.models.membership import Family
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import Model
from peewee import PrimaryKeyField


class MembershipType(str, enum.Enum):
    SEASON = 'Season'
    WEEKLY = 'Weekly'


class Membership(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, backref='memberships')
    membership_type = CharField()
    date_start = DateTimeField()
    date_end = DateTimeField()

    def get_data(self):
        return self.family, self.membership_type, self.date_start, self.date_end

    def set_end_date(self):
        if self.membership_type == MembershipType.SEASON:
            self.date_end = datetime.date(self.date_start.year, 12, 31)
        else:
            self.date_end = self.date_start + datetime.timedelta(days=6)
        self.save()

    def update_membership(
        self,
        membership_type: str | None,
        date_start: str | None,
    ) -> None:
        if membership_type:
            if membership_type in MembershipType:
                self.membership_type = membership_type
            else:
                raise MembershipTypeNotFound
        if date_start:
            try:
                date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')  # type: ignore
                self.date_start = date_start
                self.set_end_date()
            except (ValueError, TypeError):
                raise InvalidDateFormat
        self.save()

    def verify_membership_status(self, date_event: str) -> bool:
        try:
            date_event = datetime.datetime.strptime(date_event, '%Y-%m-%d')  # type: ignore
        except (ValueError, TypeError):
            raise InvalidDateFormat
        return True if self.date_start <= date_event <= self.date_end else False

    class Meta:
        database = db


with db:
    Membership.create_table(fail_silently=True)
