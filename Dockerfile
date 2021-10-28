FROM python:3.9.6
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn sql_app.main:app --reload --host 0.0.0.0 --port 8000
