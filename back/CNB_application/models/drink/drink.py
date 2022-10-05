from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import ForeignKeyField

from CNB_application.models.membership import Family

from CNB_application.core import db


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
        return True

    def buy_new_card(self) -> bool:
        self.number_of_card += 1
        self.drinks_left += 10

    class Meta:
        database = db


with db:
    Drink.create_table(fail_silently=True)
