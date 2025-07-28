FROM python:3.12

WORKDIR /tronpy_api/

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
