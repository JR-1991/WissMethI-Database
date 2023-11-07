FROM python:3.10-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python3-dev \
    && pip3 install --upgrade pip 

WORKDIR /bootstrap
COPY . /bootstrap
RUN pip3 --no-cache-dir install -r requirements.txt


ENTRYPOINT [ "python3", "./populate_db.py" ]