FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model_lr.bin", "./"]

EXPOSE 8686

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:8686", "predict:app"]

