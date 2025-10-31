FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["bash", "-c", "python create_database.py && python import_csv.py && python requete_sql.py"]