from flask import Flask, jsonify, request
from flask_cors import CORS

from repository.database_repository import FileRepository

app = Flask(__name__)
CORS(app)

repository = FileRepository()

optionsSelect = ["Agent", "Main Corp", "Accounting"]

@app.route("/get-options", methods=['GET'])
def get_options():
    #Modifica el codigo para que devuelva las opciones declaradas arriba en optionsSelect
    return jsonify({"status": 200, "data": optionsSelect})

@app.route('/save', methods=['POST'])
def save():
    #Realiza aqui tu codigo para guardar la informacion en el txt,de la forma que creas mas conveniente
    data = request.json
    repository.save_data(data)
    return jsonify({"status": 200})

@app.route('/')
def index():
    return "All Good"      

if __name__ == '__main__':
    app.run(debug=True)