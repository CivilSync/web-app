from flask import Flask
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='dein_user',
    password='dein_passwort',
    db='deine_datenbank',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def hello():
    with conn.cursor() as cursor:
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
    return f"Database time: {result['NOW()']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
