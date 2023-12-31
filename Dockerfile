FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]