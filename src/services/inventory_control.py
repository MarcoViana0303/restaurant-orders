from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        # Itera sobre cada ingrediente e a quantidade necessária na receita
        for ingredient, required_amount in recipe.items():
            # Verifica se o ingrediente não está presente
            # no estoque ou se a quantidade é menor do que a necessária
            if (
                ingredient not in self.inventory
                or self.inventory[ingredient] < required_amount
            ):
                # Retorna False se algum ingrediente não
                #  estiver disponível em quantidade suficiente
                return False
        # Retorna True se todos os ingredientes estiverem
        # disponíveis em quantidade suficiente
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        # Verifica se a receita pode ser consumida
        if self.check_recipe_availability(recipe):
            # Caso possa ser consumida, itera sobre cada
            #  ingrediente e a quantidade necessária na receita
            for ingredient, required_amount in recipe.items():
                # Subtrai a quantidade necessária
                #  de cada ingrediente do estoque
                self.inventory[ingredient] -= required_amount
        else:
            # Caso a receita não possa ser consumida,
            #  levanta uma exceção ValueError
            raise ValueError("Recipe is not available for consumption.")
