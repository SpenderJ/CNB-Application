FROM python:3.6

RUN mkdir -p /app/config
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD config/tree.json /app/config/tree.json
ADD config/config.prod.json /app/config/config.json
ENV TREE_FILE /app/config/tree.json
ENV CONFIG_FILE /app/config/config.json

ADD run.py /app/
ADD worker.py /app/

ADD CNB_application /app/template

CMD ["gunicorn","-w","1","--bind","0.0.0.0:8000","run:app"]
