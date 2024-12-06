**python version 3.10.10**

가상환경 생성
```sh
python3 -m venv venv
venv\Scripts\activate
```

가상환경 세팅
- 2024Webapp
```sh
pip install -r requirements.txt
```
- client
```sh
npm i
```

- ai
```sh
uvicorn main:app --reload
```

- client
```sh
npm run dev
```

- flask
```sh
python server.py
```
