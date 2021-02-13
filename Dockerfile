FROM tiangolo/uvicorn-gunicorn:python3.8
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy
COPY ./app /app/app
EXPOSE 5000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"] 

