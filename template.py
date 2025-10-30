import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "multi-doc-chat"

list_of_files = [
    ".github/workflows/task_defination.json",
    f"{project_name}/config/config.yaml",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/custom_exception.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/custom_logger.py",
    f"{project_name}/model/__init__.py",
    f"{project_name}/model/models.py",
    f"{project_name}/prompt/__init__.py",
    f"{project_name}/prompt/prompt_library.py",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/document_ingestion/__init__.py",
    f"{project_name}/src/document_ingestion/data_ingestion.py",
    f"{project_name}/src/document_chat/__init__.py",
    f"{project_name}/src/document_chat/retrieval.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/file_io.py",
    f"{project_name}/utils/config_loader.py",
    f"{project_name}/utils/model_loader.py",
    f"{project_name}/utils/document_ops.py",
    "notebook/01-Experiments.ipynb",
    "notebook/02-RAG.ipynb",
    "notebook/03-Evaluations.ipynb",
    "data/Agentic_AI.txt",
    "test/configure_test.py",
    "test/integration/test_chat_route.py",
    "test/integration/test_upload_route.py",
    "test/unit/test_data_ingestion.py",
    "test/unit/test_retrieval.py",
    "templates/index.html",
    "static/style.css",
    ".env",
    ".env.example",
    "main.py",
    "app.py",
    "test.py",
    "run_evaluations.py",
    ".dockerignore",
    "Dockerfile",
    "Jenkinsfile",
    "requirements.txt",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")