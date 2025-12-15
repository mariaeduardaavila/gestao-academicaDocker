from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Gestão Acadêmica Simplificada</h1>
    <p>Ambiente inicial configurado com Docker Compose e PostgreSQL </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)