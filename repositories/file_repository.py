import json
import os
from typing import List, Dict

class FileRepository:
    def __init__(self, file_path: str = "database.txt"):
        self.file_path = file_path

    def save_data(self, single_entry: Dict):
        print(f"DATA: {single_entry}")
        existing_data = {"data": []}

        # Leer el archivo si existe
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    existing_data = json.load(file)
            except json.JSONDecodeError:
                pass  # archivo vacío o mal formado

        existing_data["data"].append(single_entry)

        # Guardar el archivo actualizado
        with open(self.file_path, "w") as file:
            print(f"Guardando {len(existing_data['data'])} entradas en {self.file_path}")
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