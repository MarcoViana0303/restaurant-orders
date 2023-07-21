# Req 3
import csv
from typing import Set

from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        # Cria um conjunto vazio para armazenar os pratos
        self.dishes: Set[Dish] = set()

        with open(source_path, newline="") as csvfile:
            reader = csv.reader(csvfile)  # Cria um leitor para o arquivo CSV
            next(reader)  # Pula a linha do cabeçalho

            for row in reader:  # Itera sobre as linhas do arquivo
                dish_name = row[0]  # Obtém o nome do prato da coluna 0
                # Obtém o preço do prato da coluna 1
                dish_price = float(row[1])
                # Obtém o nome do ingrediente da coluna 2
                ingredient_name = row[2]
                # Obtém a quantidade do ingrediente da coluna 3
                ingredient_quantity = int(row[3])
                # Instancia o ingrediente com o nome
                ingredient = Ingredient(ingredient_name)
                dish = next(
                    (d for d in self.dishes if d.name == dish_name),
                    None
                )  # Procura o prato pelo nome no conjunto de pratos existentes

                if dish is None:  # Se o prato ainda não existe
                    dish = Dish(dish_name, dish_price)  # Cria um novo prato
                    # Adiciona o prato ao conjunto de pratos
                    self.dishes.add(dish)

                # Adiciona a dependência de ingrediente ao prato
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

