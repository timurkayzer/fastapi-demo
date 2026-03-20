FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

# Run migrations and start app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]