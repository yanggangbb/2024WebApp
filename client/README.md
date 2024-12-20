# **프로젝트 기획서**

## **1. 프로젝트 개요**
### **프로젝트 제목**  
**"실습실 및 대여 관리 시스템 개발"**

### **목적**  
- 실습실과 기기 대여 과정을 디지털화하여 편리성과 효율성을 증대.  
- 교실 및 기기의 정보와 사용 현황을 투명하게 관리.  
- AI 기술을 활용하여 사용자 경험 향상 및 효율적인 자원 활용 가능.

---

## **2. 주요 기능 정의**

### **(1) 실습실 사용 신청 및 관리**
1. **교실 정보 표시**
   - 교실 단면도를 통해 클릭 시 컴퓨터 사양, 설치 프로그램, 사용 가능 대수를 표시.
   - 예시 정보: 
     - CPU: Intel i7  
     - GPU: RTX 3070  
     - 설치 프로그램: Python, Unity, Adobe Creative Cloud 등  
     - 컴퓨터 개수: 20대  

2. **사용 신청**
   - 사용자가 학번과 이름을 입력하여 실습실 사용 신청.  
   - 사용 시작 시간 및 종료 시간 기록.  

3. **신청 현황 확인**
   - 신청된 내역(학번, 이름, 사용 시작~종료 시간)을 조회 가능.

---

### **(2) 노트북/태블릿 대여 관리**
1. **대여 정보 입력**
   - 학번, 이름, 대여 기기(노트북/태블릿) 선택 후 신청.  
   - 대여 기기 사용 가능 여부 확인 가능.  

2. **대여 기록 관리**
   - 현재 대여 중인 기기와 사용자 정보 확인.  
   - 반납 시간 기록 및 자동화된 연체 알림 제공.  

---

### **(3) 빈 교실 사용 신청**
1. **교실 정보 확인**
   - 사용 가능한 교실 목록 표시.  
   - 교실 단면도를 통해 교실 정보 및 상태 확인.

2. **사용 신청**
   - 학번, 이름, 이용 시간 입력하여 신청.  
   - 신청 내역 저장 및 현황 관리.  

---

### **(4) 교실 단면도 및 신청 시스템**
1. **교실 단면도**
   - 교실 단면도 클릭 시 해당 교실의 상세 정보(컴퓨터 성능, 개수, 설치 프로그램 등) 표시.  

2. **신청 버튼**
   - 사용 신청 버튼을 통해 바로 사용 신청 가능.  
   - 신청 현황 버튼으로 교실별 신청 기록 확인 가능.  

3. **조교실 대여 서비스**
   - 조교실 클릭 시 노트북 및 태블릿 대여 서비스 화면으로 이동.

---

## **3. AI 기능 추가 아이디어**

### **(1) 실시간 교실 추천 시스템**
1. **기능**
   - 사용자가 원하는 사양(예: 그래픽카드 성능, 설치 프로그램 등)을 입력하면 AI가 현재 사용 가능한 교실 중 가장 적합한 교실을 추천.

2. **활용 기술**
   - **Python + 머신러닝 모델**: 협업 필터링 기반 추천 시스템 구현.  
   - Flask REST API로 AI 기능과 사용자 인터페이스 연결.

3. **필요 데이터**
   - 교실별 사양 및 설치 프로그램 정보.  
   - 시간대별 교실 사용 현황 데이터.

4. **구현 방식**
   - 사용자 요구사항(예: 프로그램 종류, GPU 사양) 입력.  
   - AI 모델이 사용 가능한 교실 데이터를 바탕으로 적합도를 계산하여 추천.  

5. **기대 효과**
   - 사용자는 적합한 교실을 빠르게 찾을 수 있음.  
   - 자원의 효율적 활용 가능.

---

## **4. 기술 스택**

### **백엔드**
- Flask (Python 기반, 가볍고 빠른 API 개발 가능)
- Firebase (클라우드 기반 데이터베이스)

### **프론트엔드**
- HTML, CSS, JavaScript  
- 선택적으로 React.js를 활용한 동적 UI 구성 가능.

### **AI**
- Scikit-learn 또는 PyTorch 기반 머신러닝 모델.  
- 협업 필터링, 조건 필터링 등의 알고리즘 활용.
- 허깅페이스에서 찾아보기

---

## **5. 데이터 설계**
---

## **6. 기대 효과**
1. **관리 효율성 증대**  
   - 모든 신청 및 관리 과정을 디지털화하여 업무 부담 감소.

2. **사용자 만족도 향상**  
   - 교실 및 기기의 실시간 정보 제공으로 편리성 증대.  
   - AI 기반 추천 시스템으로 사용자 요구를 더 잘 충족.  

3. **자원 활용 최적화**  
   - 교실과 기기의 사용률을 분석하여 효율적으로 자원을 관리.

---
