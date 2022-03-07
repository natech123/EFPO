ENV PATH \\wsl$\Ubuntu\home\coolyo\code\natech123\EFPO

FROM python:3.8.6-buster

COPY api
COPY EFPO
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
