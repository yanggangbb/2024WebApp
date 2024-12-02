from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer, util
import sqlite3

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 초기 데이터
lab_data = {
    "302": {
        "cpu": "Intel(R) Core(TM) i7-9700",
        "gpu": "NVIDIA GeForce RTX 2060",
        "memory": "16GB",
        "disk": "SSD 970 PRO 512GB",
        "program": "Adobe Creative Cloud, AutoCAD, Eclipse, IntelliJ, Node.js, Oracle Database, PyCharm, QGIS, Visual Studio, Visual Studio Code",
        "language": "Java, Python, R",
        "Notes": "멀티탭 2자리 1개",
        "count": "27",
        "image_url": "/static/images/302.jpg"
    },
    "306": {
        "cpu": "Intel(R) Core(TM) i9-13700",
        "gpu": "NVIDIA GeForce RTX 4060",
        "memory": "32GB",
        "disk": "SAMSUNG MZVL2512HCJQ-00B00",
        "program": "Adobe Creative Cloud, Visual Studio, Unity, Unreal Engine",
        "language": "-",
        "Notes": "성능은 좋지만 깔린게 없음",
        "count": "24",
        "image_url": "/static/images/306.jpg"
    },
    "307": {
        "cpu": "Intel(R) Core(TM) i7-9700",
        "gpu": "NVIDIA GeForce RTX 2060",
        "memory": "16GB",
        "disk": "SSD 970 PRO 512GB",
        "program": "Adobe Creative Cloud, Visual Studio Code",
        "language": "Java",
        "Notes": "인터넷 느림, 멀티탭 2자리 1개",
        "count": "25",
        "image_url": "/static/images/307.jpg"
    },
    "308": {
        "cpu": "Intel(R) Core(TM) i7-9700",
        "gpu": "NVIDIA GeForce RTX 3060",
        "memory": "32GB",
        "disk": "SSD 970 PRO 512GB",
        "program": "Adobe Creative Cloud, AutoCAD, CUDA, Eclipse, IntelliJ, Node.js, Oracle Database, PyCharm, QGIS, Visual Studio, Visual Studio Code",
        "language": "Java, Python, R",
        "Notes": "없음",
        "count": "26",
        "image_url": "/static/images/308.jpg"
    }
}

# 데이터베이스 초기화
def init_lab_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS labs (
            id TEXT PRIMARY KEY,
            cpu TEXT,
            gpu TEXT,
            memory TEXT,
            disk TEXT,
            program TEXT,
            language TEXT,
            notes TEXT,
            count INTEGER,
            image_url TEXT
        )
    ''')

    for lab_id, lab_info in lab_data.items():
        cursor.execute('''
            INSERT OR IGNORE INTO labs (id, cpu, gpu, memory, disk, program, language, notes, count, image_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            lab_id,
            lab_info["cpu"],
            lab_info["gpu"],
            lab_info["memory"],
            lab_info["disk"],
            lab_info["program"],
            lab_info["language"],
            lab_info["Notes"],
            int(lab_info["count"]),
            lab_info["image_url"]
        ))

    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/computer/<id>')
def get_computer(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM labs WHERE id = ?', (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        lab_info = {
            "id": row[0],
            "cpu": row[1],
            "gpu": row[2],
            "memory": row[3],
            "disk": row[4],
            "program": row[5],
            "language": row[6],
            "Notes": row[7],
            "count": row[8],
            "image_url": row[9]
        }
        return jsonify(lab_info)
    else:
        return jsonify({"error": "Data not found"}), 404

@app.route('/recommend', methods=['POST'])
def recommend_lab():
    user_request = request.json['description']
    user_embedding = model.encode(user_request, convert_to_tensor=True)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, program FROM labs')
    rows = cursor.fetchall()
    conn.close()

    scores = []
    for lab_id, program in rows:
        lab_embedding = model.encode(program, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(user_embedding, lab_embedding).item()
        scores.append({"id": lab_id, "score": similarity})

    best_match = max(scores, key=lambda x: x['score'])
    return jsonify(best_match)

if __name__ == '__main__':
    init_lab_data()
    app.run(debug=True)
