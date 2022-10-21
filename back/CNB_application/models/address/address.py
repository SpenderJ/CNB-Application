from __future__ import annotations

from CNB_application.core import db
from CNB_application.models.membership import Family
from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField


class Address(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, unique=True)
    address = CharField()
    city = CharField()
    zip_code = IntegerField()
    country = CharField()

    def update_address(
        self,
        address: str | None,
        city: str | None,
        zip_code: int | None,
        country: str | None,
    ) -> None:
        self.address = address if address else self.address
        self.city = city if city else self.city
        self.zip_code = zip_code if zip_code else self.zip_code
        self.country = country if country else self.country
        self.save()

    def get_data(self):
        return self.family, self.address, self.city, self.zip_code, self.country

    class Meta:
        database = db


with db:
    Address.create_table(fail_silently=True)
