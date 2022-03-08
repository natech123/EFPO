FROM python:3.8.6-buster
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



COPY api.py /api.py
COPY EFPO /EFPO
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
