from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade TEXT,
            class TEXT,
            number TEXT,
            name TEXT,
            purpose TEXT,
            date TEXT,
            start_time TEXT,
            end_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/reservations', methods=['GET'])
def get_reservations():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    rows = cursor.fetchall()
    conn.close()

    reservations = [
        {
            "id": row[0],
            "grade": row[1],
            "class": row[2],
            "number": row[3],
            "name": row[4],
            "purpose": row[5],
            "date": row[6],
            "start_time": row[7],
            "end_time": row[8],
        }
        for row in rows
    ]

    return jsonify(reservations)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
