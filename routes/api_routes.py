from flask import Blueprint, jsonify, request
from repositories.file_repository import FileRepository

api = Blueprint("api", __name__)
repository = FileRepository()

optionsSelect = ["Agent", "Main Corp", "Accounting"]

@api.route("/get-options", methods=["GET"])
def get_options():
    return jsonify({"status": 200, "options": optionsSelect})

@api.route("/save", methods=["POST"])
def save():
    data = request.json
    print("Guardando...", data)
    repository.save_data(data)
    return jsonify({"status": 200})

@api.route("/", methods=["GET"])
def index():
    return "All Good"