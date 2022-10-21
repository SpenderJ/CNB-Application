from __future__ import annotations

from CNB_application.core import db
from CNB_application.models.membership import Family
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField


class Drink(Model):
    id = PrimaryKeyField()
    family = ForeignKeyField(Family, unique=True)
    drinks_left = IntegerField()
    number_of_card = IntegerField()

    def get_data(self):
        return self.family, self.drinks_left, self.number_of_card

    def consume_drink(self) -> bool:
        if self.drinks_left == 0:
            return False
        self.drinks_left -= 1
        self.save()
        return True

    def buy_new_card(self) -> bool:
        self.number_of_card += 1
        self.drinks_left += 10
        self.save()
        return True

    def update_drink_card(
        self,
        drinks_left: int | None,
        number_of_card: int | None,
    ) -> None:
        self.drinks_left = drinks_left if drinks_left else self.drinks_left
        self.number_of_card = number_of_card if number_of_card else self.number_of_card
        self.save()

    class Meta:
        database = db


with db:
    Drink.create_table(fail_silently=True)
