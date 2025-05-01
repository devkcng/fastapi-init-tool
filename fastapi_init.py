import os
import argparse

# Default structure for FastAPI project
project_structure = {
    "app": {
        "__init__.py": [],
        "api": ["__init__.py", "routes.py"],
        "core": ["__init__.py", "config.py"],
        "models": ["__init__.py"],
        "services": ["__init__.py"],
        "utils": ["__init__.py"],
    }
}


def get_project_files(project_name):
    return {
        "requirements.txt": "fastapi[all]\npython-dotenv\n",
        ".env.dev": f"ENV=development\nPROJECT_NAME={project_name}\n",
        ".gitignore": "__pycache__/\n.env\n.venv/\n*.pyc\n",

        "app/main.py": f'''from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="{project_name}")

app.include_router(router)
''',

        "app/api/routes.py": '''from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "FastAPI AI App is running!"}
''',

        "app/core/config.py": '''import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "AI API")
    API_VERSION: str = "1.0"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
''',

        "Dockerfile": '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the environment file
COPY .env.dev .

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
''',

        "docker-compose.yml": '''version: '3.8'

services:
  fastapi:
    build: .
    container_name: fastapi-ai
    volumes:
      - .:/app
      - ./requirements.txt:/requirements.txt
    ports:
      - "8000:8000"
    environment:
      - ENV=development
    env_file:
      - .env.dev
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
''',

        "PROJECT_README.md": f'''# {project_name}

## Installation

### On Linux/Mac
1. Install Python 3.11 and dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```

### On Windows
1. Install Python 3.11 and dependencies:
    ```powershell
    python -m venv .venv
    .\\.venv\\Scripts\\activate
    pip install -r requirements.txt
    ```

2. Run the server:
    ```powershell
    uvicorn app.main:app --reload
    ```

### Using Docker
1. Build the Docker image:
    ```bash
    docker-compose up --build
    ```

2. Visit the app:
    - **API:** http://localhost:8000
    - **Swagger UI:** http://localhost:8000/docs
'''
    }

def create_structure(base_path, project_name):
    for folder, subfolders in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for subfolder, files in subfolders.items():
            # If subfolder is a file (e.g. "__init__.py" at top-level)
            if isinstance(files, list):
                subfolder_path = os.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                for file in files:
                    file_path = os.path.join(subfolder_path, file)
                    open(file_path, "w").close()
            else:
                # subfolder is actually a file
                file_path = os.path.join(folder_path, subfolder)
                open(file_path, "w").close()

def create_files(base_path, project_name):
    # Get files with the provided project name
    project_files = get_project_files(project_name)
    for path, content in project_files.items():
        file_path = os.path.join(base_path, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def prompt_for_project_name():
    project_name = input("Enter the project name (leave blank to use current directory '.' as the name): ")
    if not project_name or project_name == ".":
        project_name = os.path.basename(os.getcwd())  # Use current directory name if user enters '.'
    return project_name

def parse_args():
    parser = argparse.ArgumentParser(description="Generate FastAPI project structure")
    parser.add_argument(
        "--init",
        action="store_true",
        help="Generate FastAPI project with Docker and example files",
    )
    parser.add_argument(
        "--name",
        type=str,
        help="Name of the project (e.g., MyAIApp)",
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    if args.init:
        project_name = args.name if args.name else prompt_for_project_name()

        # Determine base path: if project_name is '.', use current directory
        if args.name == "." or (not args.name and project_name == os.path.basename(os.getcwd())):
            base_path = os.getcwd()
        else:
            base_path = os.path.join(os.getcwd(), project_name)
            if not os.path.exists(base_path):
                os.makedirs(base_path)
        
        print(f"Initializing FastAPI project: {project_name}...")
        create_structure(base_path, project_name)
        create_files(base_path, project_name)
        print(f"✅ {project_name} project initialized successfully. Check PROJECT_README.md for instructions.")
    else:
        print("❌ No action specified. Use --init to generate the project.")

if __name__ == "__main__":
    main()
