from __future__ import annotations

from CNB_application.core import db
from peewee import BooleanField
from peewee import CharField
from peewee import Model
from peewee import PrimaryKeyField


class Family(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    phone_number = CharField(null=True)
    benefactor_member = BooleanField(default=False)
    parking = BooleanField(default=False)

    @property
    def address(self):
        return self.address_set.get()

    @property
    def drink(self):
        return self.drink_set.get()

    def update_family(
        self,
        first_name: str | None,
        last_name: str | None,
        email: str | None,
        phone_number: str | None,
        benefactor_member: bool | None,
        parking: bool | None,
    ) -> None:
        self.first_name = first_name if first_name else self.first_name
        self.last_name = last_name if last_name else self.last_name
        self.email = email if email else self.email
        self.phone_number = phone_number if phone_number else self.phone_number
        self.benefactor_member = (
            benefactor_member if benefactor_member else self.benefactor_member
        )
        self.parking = parking if parking else self.parking
        self.save()

    def get_data(self):
        return (
            self.first_name,
            self.last_name,
            self.email,
            self.phone_number,
            self.benefactor_member,
            self.parking,
        )

    def get_family(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
        }

    class Meta:
        indexes = ((('first_name', 'last_name'), True),)
        database = db


with db:
    Family.create_table(fail_silently=True)
