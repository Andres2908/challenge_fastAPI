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


```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Envs
It considers that version 3 of virusTotal is being used, since v2 appears to be obsolete.

https://www.virustotal.com/api/v3

## Build docker

```bash
docker-compose up --build
```

## Run Docker

To run the application with Docker, use the following command:

```bash
docker-compose start
```