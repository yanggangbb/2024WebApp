pip install Flask sentence-transformers torch

Python 3.10.10(최신버전은 torch가 안되는듯)

Hugging Face 모델 사용함

app.py 실행시키면 됨


지피티 피셜 = [

작동 방식
(1) 사용자 입력
웹 페이지에서 사용자가 텍스트를 입력하고 추천 버튼을 누릅니다.
예: "Unity와 Unreal Engine을 사용하는 고성능 컴퓨터가 필요해요."
(2) 서버에서 작업 처리
입력 데이터 처리: 사용자가 입력한 문장을 받아 분석.
유사도 계산:
서버가 사전에 저장된 실습실 데이터와 사용자의 요청을 비교.
SentenceTransformer 모델을 사용해 입력 문장과 각 실습실의 설명을 숫자로 변환(임베딩).
변환된 숫자 벡터 간 코사인 유사도를 계산하여 얼마나 비슷한지 점수화.
가장 적합한 실습실 선택:
모든 실습실과 유사도를 비교해 가장 높은 점수를 가진 실습실을 선택.
(3) 결과 반환
선택된 실습실의 이름, 유사도 점수, 기타 정보를 사용자에게 JSON 형식으로 반환.
(4) 결과 출력
웹 페이지에 추천된 실습실 이름과 점수가 표시됩니다.
예: "추천 실습실: 306호, 유사도 점수: 0.92"

]

가상환경 생성 > pip install -r requirements.txt

```sh
python3 -m venv venv
venv\Scripts\activate
```
