import json
import os
from typing import List, Dict

class FileRepository:
    def __init__(self, file_path: str = "database.txt"):
        self.file_path = file_path

    def save_data(self, data):
        existing_data = {"item": []}

        # Leer si el archivo existe
        if os.path.exists(self.file_path):
            # Intentar cargar el contenido existente
            with open(self.file_path, "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    pass  # si el archivo está vacío o mal formado

        # Agregar nuevo item
        new_item = data.get("item")
        if new_item:
            if new_item not in existing_data["item"]:
                existing_data["item"].append(new_item)

        # Escribir nuevamente todo el contenido
        with open(self.file_path, "w") as file:
            json.dump(existing_data, file, indent=2)

    def read_all(self) -> List[Dict]:
        results = []
        try:
            # Leer el archivo línea por línea
            with open(self.file_path, "r") as file:
                # Cargar cada línea como un objeto JSON
                for line in file:
                    results.append(json.loads(line))
        # Manejar el caso en que el archivo no exista o esté vacío
        except FileNotFoundError:
            pass
        return results