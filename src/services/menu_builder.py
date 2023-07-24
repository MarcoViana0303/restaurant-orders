from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        # Inicializa uma lista vazia para armazenar os pratos do menu
        menu = []

        # Obtém a lista de pratos disponíveis no cardápio a
        # partir do atributo dishes da instância de "MenuData"
        dishes = self.menu_data.dishes

        # Inicia um loop que itera sobre cada prato disponível no cardápio
        for dish in dishes:
            # Verifica se há uma restrição alimentar especificada
            if restriction:
                # Filtra os pratos que possuem a restrição alimentar
                dishes = [dish for dish in dishes if
                          restriction in dish.get_restrictions()
                          ]

            # Verifica se a restrição não está
            #  presente nas restrições do prato atual
            if restriction not in dish.get_restrictions():
                # Cria um dicionário com os dados do prato atual
                dish_data = {
                    "dish_name": dish.name,
                    "ingredients": dish.get_ingredients(),
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                }
                # Adiciona o dicionário com os dados do prato à lista do menu
                menu.append(dish_data)

        # Retorna a lista de pratos disponíveis no menu
        return menu
