FROM tiangolo/uvicorn-gunicorn:python3.8
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy
COPY ./app /app/app


