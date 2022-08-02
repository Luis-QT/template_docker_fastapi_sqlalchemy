FROM python:3.9

RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev

COPY ./ /app
WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

CMD uvicorn app.main:app --reload --host=0.0.0.0 --port=${PORT:-8080}

# CMD exec gunicorn --bind :8080 --workers 1 --worker-class uvicorn.workers.UvicornWorker --timeout 0 app.main:app
