FROM python:slim

RUN useradd searcher

WORKDIR /home/searchapi

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

#COPY app orm_search
COPY searchapi.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP searchapi.py

RUN chown -R searcher:searcher ./
USER searcher

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]