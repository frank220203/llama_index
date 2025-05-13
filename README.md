# llama_index
### 개요
- 개발 환경 : FastAPI, uvicorn
- DB : PostgreSQL

### FastAPI 설치 방법
```bash
# FastAPI 라이브러리 
pip install fastapi
# FastAPI 서드파티 라이브러리 (ex. cbv)
pip install fastapi-utils
pip install typing-inspect
# asyncio 비동기 처리가 가능한 서버
pip install uvicorn
# App 설정
pip install pydantic-settings
```

### FastAPI 실행 방법
```bash
# app 디렉토리로 이동
cd app
# 서버 실행
uvicorn main:app --port 8001 --reload
```

### LlamaIndex 설치
```bash
# Llm 라이브러리
pip install llama_index
# 벡터 저장소 번들
pip install llama-index-vector-stores-postgres
# google-genai Python SDK
pip install llama-index-llms-google-genai
pip install llama-index-embeddings-ollama
pip install llama-index-embeddings-google-genai
```

### PostgreSQL 연동
```bash
# psycopg 드라이버 사용
pip install "psycopg[binary]"
```

### Test 진행
```bash
# pytest 설치
pip install pytest
# 비동기 요청 테스트 라이브러리
pip install trio
# test.py 만들고, 테스트 실행
pytest
# 단일 테스트 실행
pytest -k "test_submit_query" ./tests/domain/usecases/test_channel_usecase.py
```

### 기타
```text
# async(비동기) 처리
1. 외부 API 호출
2. DB 사용
3. 파일 I/O 처리

# 일반 함수 호출
1. 패키지에 설치된 라이브러리 호출 등등

# PostgreSQL
원도우 설치는 권한부족으로 PostgreSQL 11버전 설치
```