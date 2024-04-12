FROM python:3.9-slim-buster

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["chainlit", "run", "main.py", "--port", "8501"]

