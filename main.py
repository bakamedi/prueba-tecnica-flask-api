from flask import Flask
from flask_cors import CORS
from routes.api_routes import api  # Importas el Blueprint

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

app.register_blueprint(api)  # Registras las rutas

if __name__ == "__main__":
    app.run(debug=True)