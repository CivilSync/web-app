from flask import Flask, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# DB-Konfiguration über Umgebungsvariablen
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST', 'mariadb')
app.config['MYSQL_USER'] = os.environ.get('DB_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME', 'testdb')

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT 'Hello from MariaDB!'")
    result = cur.fetchone()
    cur.close()
    return jsonify(message=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
