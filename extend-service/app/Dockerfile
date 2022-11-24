FROM python:3.8-slim

ENV APP_PORT=5000
ENV MODE=local

ARG BASE_PATH=/flask-application

WORKDIR ${BASE_PATH}

RUN addgroup --system flaskgroup
RUN adduser --system --disabled-password flaskuser 
RUN adduser flaskuser flaskgroup
RUN chown -R flaskuser:flaskgroup ${BASE_PATH}

USER flaskuser

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${APP_PORT}

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]