# challenge_fastAPI

## Requirements

- python3.9
- pip

## Installation Local

Activate the virtual environment

whit venv python
```bash
python3 -m venv .venv
. .venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt --no-cache
```

To run the application locally:

```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

## Run Docker

To run the application with Docker, use the following command:

```bash
docker-compose up --build
```