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

## Evaluations 🧪

Run LangSmith evaluations on your RAG system:

```bash
# Quick start - run with default settings
python run_evaluations.py

# Run with all evaluators
python run_evaluations.py --evaluator all

# Custom parameters
python run_evaluations.py --evaluator correctness --chunk-size 500 --k 10
```

**Available Evaluators:**

- `correctness` - Custom LLM-as-a-Judge (Gemini 2.5 Pro)
- `cot_qa` - Chain-of-Thought QA evaluator
- `all` - Run all evaluators

**Documentation:**

- Jupyter Notebook: [notebook/03-Evaluations.ipynb](notebook/03-Evaluations.ipynb)
- MMR Implementation: [guide/MMR_IMPLEMENTATION.md](guide/MMR_IMPLEMENTATION.md)

## Notes

- Ensure your API keys/config are set for the `ModelLoader` to load embeddings/LLM.
- For evaluations, you need `LANGSMITH_API_KEY` and `GOOGLE_API_KEY` in your `.env` file.
- Supported file types: `.pdf`, `.docx`, `.txt`.
- For production, add persistence for chat history and auth; consider cleanup of old session directories.

## Deployment

### Deployed to AWS ECS Fargate via CI/CD using GitHub Actions

### **IAM User Attached Policies**

**Custom Policies**
1- AllowECSLogs        -> [guide/allow_ecs_logs.json](guide/allow_ecs_logs.json)
2- AllowSecretsAccess  -> [guide/allow_secrets_access.json](guide/allow_secrets_access.json)
But Here (AllowSecretsAccess) You Must First Create The Secret In AWS Secrets Manager Manually With Custom Key and Value

**AWS Managed Policies**
3- AmazonEC2ContainerRegistryFullAccess
4- AmazonECS_FullAccess
5- AmazonS3FullAccess
6- CloudWatchLogsFullAccess
7- SecretsManagerReadWrite
