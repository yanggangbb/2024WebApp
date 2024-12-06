from sentence_transformers import SentenceTransformer
import numpy as np
import json
from scipy.spatial.distance import cosine

# Sentence Transformer 모델 로드
model = SentenceTransformer('all-MiniLM-L6-v2')

# 교실 데이터 불러오기
def load_classroom_data():
    with open('app/data/lab_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 교실 데이터 로드
classrooms = load_classroom_data()

# CPU 성능 정의
cpu_performance = {
    "매우높음": ["Intel(R) Core(TM) i9-13700"],
    "높음": ["Intel(R) Core(TM) i7-9700"]
}

# GPU 성능 정의
gpu_performance = {
    "매우높음": ["NVIDIA GeForce RTX 4090"],
    "높음": ["NVIDIA GeForce RTX 3060"],
    "중간": ["NVIDIA GeForce RTX 2060"]
}

# 활동 요구사항 정의 함수
def get_activity_requirements(activity: str):
    requirements = {
        "AI 개발": {
            "description": "Python, TensorFlow, CUDA 지원 GPU",
            "cpu": "높음 ~ 매우높음",
            "gpu": "매우높음 ~ 높음",
            "program": ["CUDA", "Visual Studio Code", "TensorFlow", "PyTorch"],
            "language": ["Python"]
        },
        "웹 개발": {
            "description": "Node.js, Visual Studio Code",
            "cpu": "높음",
            "gpu": "높음 ~ 중간",
            "program": ["Visual Studio Code", "Node.js", "Eclipse", "Oracle Database"],
            "language": ["Python", "Java"]
        },
        "앱 개발": {
            "description": "Visual Studio Code, Android Studio, Oracle Database, IntelliJ 등",
            "cpu": "높음",
            "gpu": "높음 ~ 중간",
            "program": ["Visual Studio Code", "Android Studio", "IntelliJ", "Oracle Database"],
            "language": ["Python", "Java"]
        },
        "데이터 분석": {
            "description": "Python, R 등",
            "cpu": "높음",
            "gpu": "높음 ~ 중간",
            "program": ["Visual Studio Code", "Jupyter Notebook", "RStudio"],
            "language": ["Python", "R"]
        },
        "게임 개발": {
            "description": "Unity, Unreal Engine 등",
            "cpu": "매우높음 ~ 높음",
            "gpu": "매우높음 ~ 높음",
            "program": ["Unity", "Unreal Engine"],
            "language": "-"
        },
        "그래픽": {
            "description": "Adobe Creative Cloud, Zbrush, Substance 등",
            "cpu": "매우높음 ~ 높음",
            "gpu": "매우높음 ~ 높음",
            "program": ["Adobe Creative Cloud", "Zbrush", "Substance", "바디페인트"],
            "language": "-"
        },
        "지도제작": {
            "description": "AutoCAD 등",
            "cpu": "높음 ~ 중간",
            "gpu": "높음 ~ 중간",
            "program": ["AutoCAD"],
            "language": "-"
        },
        "공간정보": {
            "description": "QGIS 등",
            "cpu": "높음 ~ 중간",
            "gpu": "높음 ~ 중간",
            "program": ["QGIS"],
            "language": ["Python"]
        }
    }
    return requirements.get(activity, {
        "description": "Default requirements",
        "cpu": [],
        "gpu": [],
        "program": [],
        "language": []
    })

# 키워드 기반 활동 매핑 함수
def map_activity_by_keywords(activity: str):
    keyword_map = {
        "AI": "AI 개발",
        "인공지능": "AI 개발",
        "ai": "AI 개발",
        "Ai": "AI 개발",
        "웹": "웹 개발",
        "앱": "앱 개발",
        "애플리케이션": "앱 개발",
        "데이터": "데이터 분석",
        "게임": "게임 개발",
        "그래픽": "그래픽",
        "지도": "지도제작",
        "공간정보": "공간정보"
    }
    for keyword, mapped_activity in keyword_map.items():
        if keyword.lower() in activity.lower():  # 대소문자 구분 없이 매핑
            return mapped_activity
    return activity


# 교실 추천 함수
def recommend_based_on_activity(activity: str):
    # 키워드 기반 활동 매핑
    mapped_activity = map_activity_by_keywords(activity)
    activity_requirements = get_activity_requirements(mapped_activity)

    # 활동과 교실 간 임베딩 유사도 계산
    activity_embedding = model.encode([activity_requirements['description']])
    classroom_embeddings = [
        model.encode(f"{c['cpu']} {c['gpu']} {c['memory']} {', '.join(c['program'])}") 
        for c in classrooms.values()
    ]
    similarities = [
        1 - cosine(activity_embedding[0], classroom_embedding)
        for classroom_embedding in classroom_embeddings
    ]

    # 추가 점수 계산 (프로그램, 언어 지원)
    program_scores = []
    language_scores = []
    for classroom in classrooms.values():
        program_score = sum(1 for req_program in activity_requirements['program'] if req_program in classroom['program'])
        language_score = sum(1 for req_language in activity_requirements['language'] if req_language in classroom['language'])
        program_scores.append(program_score)
        language_scores.append(language_score)

    # 점수 정규화
    def normalize(scores):
        max_score = max(scores) if max(scores) > 0 else 1
        return [score / max_score for score in scores]

    normalized_similarities = normalize(similarities)
    normalized_program_scores = normalize(program_scores)
    normalized_language_scores = normalize(language_scores)

    # 가중치 적용
    total_scores = [
        0.4 * normalized_similarities[i] +
        0.4 * normalized_program_scores[i] +
        0.2 * normalized_language_scores[i]
        for i in range(len(classrooms))
    ]

    # 가장 높은 점수를 가진 교실 선택
    best_match_index = np.argmax(total_scores)
    best_classroom_id = list(classrooms.keys())[best_match_index]
    best_classroom = classrooms[best_classroom_id]

    # 설명 개선
    required_programs = activity_requirements['program']
    matched_programs = [prog for prog in required_programs if prog in best_classroom['program']]
    matched_programs_str = ', '.join(matched_programs)

    # 설명 문자열 생성
    explanation = (
        f"{activity}에 가장 적합한 교실은 {best_classroom_id}호입니다. "
        f"이 교실은 {best_classroom['cpu']}와 {best_classroom['gpu']}를 갖추고 있으며, "
        f"{matched_programs_str} 프로그램을 지원합니다."
    )
    
    return best_classroom_id, explanation
