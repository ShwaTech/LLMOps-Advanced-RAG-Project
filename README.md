# LLMOps-Advanced-RAG-Project

End-To-End Advanced RAG Project: build an Advanced RAG with LangChain, FAISS DB, and utilizing advanced features (Memory, Evaluations - DeepEval, LLM as Judge, MMR - Maximal Marginal Relevance); integrate with FastAPI APIs and UI (Streamlit/HTML/CSS); test using Pytest; and finally deploy to AWS ECS Fargate via CI/CD using GitHub Actions and Jenkins...

## Project Structure

```bash
LLMOps-Advanced-RAG-Project/
├── .github/
│   └── workflows/
│       └── task_defination.json
│
├── multi-doc-chat/
│   ├── config/
│   │   └── config.yaml
│   │
│   ├── exception/
│   │   ├── __init__.py
│   │   └── custom_exception.py
│   │
│   ├── logger/
│   │   ├── __init__.py
│   │   └── custom_logger.py
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── prompt/
│   │   ├── __init__.py
│   │   └── prompt_library.py
│   │
│   ├── src/
│   │   ├── __init__.py
│   │   ├── document_ingestion/
│   │   │   ├── __init__.py
│   │   │   └── data_ingestion.py
│   │   │
│   │   └── document_chat/
│   │       ├── __init__.py
│   │       └── retrieval.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── file_io.py
│       ├── config_loader.py
│       ├── model_loader.py
│       └── document_ops.py
│
├── notebook/
│   ├── 01-Experiments.ipynb
│   ├── 02-RAG.ipynb
│   └── 03-Evaluations.ipynb
│
├── test/
│   ├── configure_test.py
│   ├── integration/
│   │   ├── test_chat_route.py
│   │   └── test_upload_route.py
│   └── unit/
│       ├── test_data_ingestion.py
│       └── test_retrieval.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── main.py
├── app.py
├── test.py
├── run_evaluations.py
├── .dockerignore
├── Dockerfile
├── Jenkinsfile
└── requirements.txt
```

## Environment Setup

```bash
# Initialize The Project
uv init

# This Command Will Automatically Create A Virtual Environment And Install All The Dependencies
uv add -r requirements.txt

# Activate The Virtual Environment
source .venv/bin/activate
```

## MultiDocChat (FastAPI)

### How it works

- Upload: Files are uploaded to `data/<session_id>/`, split, embedded, and saved as a FAISS index in `faiss_index/<session_id>/`.
- Chat: Each request loads the FAISS index for the given `session_id` and answers using RAG.
- Sessions: A simple in-memory history per session on the server (resets on restart). The browser stores `session_id` in `localStorage`.

### Run locally

1- Install deps

```bash
pip install -r requirements.txt
```

2- Start the server

```bash
uvicorn main:app --reload
```

3- Open the UI

```bash
open http://localhost:8000/
```

### Endpoints

- `GET /` – Serves the UI.
- `GET /health` – Health check.
- `POST /upload` – Form-data file upload. Returns `{ session_id, indexed }`.
- `POST /chat` – JSON body `{ session_id, message }`. Returns `{ answer }`.
