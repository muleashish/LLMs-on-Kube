FROM python:3.9

COPY . .

RUN pip install -r requirements.txt

RUN pip install --default-timeout=100 torch-2.2.2-cp39-cp39-manylinux1_x86_64.whl

EXPOSE 8001

CMD ["python", "main.py"]