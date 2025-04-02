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
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Envs
It considers that version 3 of virusTotal is being used, since v2 appears to be obsolete.

https://www.virustotal.com/api/v3

## 🐳 Docker compose

Build:
```bash
docker-compose up --build
```

Start the containers
```bash
docker-compose start  
```

stop container
```bash
docker-compose stop
```

## 🐳 Dockerfile

Build:
```bash
docker build -t image-name .
```

Run container
```bash
docker run --name name-container -d -p 8000:8000 name-image
```

## Test in docker-compose

Container test:
```bash
docker-compose up tests
```

