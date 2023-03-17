FROM python:3.10.4

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /

CMD [ "uvicorn", "app.application:project_app", "--host", "0.0.0.0", "--port", "80", "--reload"]