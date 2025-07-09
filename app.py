from flask import Flask
import pymysql
import os

app = Flask(__name__)

# Konfiguration aus Umgebungsvariablen
DB_HOST = os.environ.get('DB_HOST', 'mariadb')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'testdb')

@app.route('/')
def hello():
    try:
        # Verbindung bei jedem Request herstellen
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW()")
            result = cursor.fetchone()
        conn.close()
        return f"Database time: {result['NOW()']}"
    except Exception as e:
        return f"Fehler bei DB-Zugriff: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)