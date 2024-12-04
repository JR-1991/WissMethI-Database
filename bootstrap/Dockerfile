FROM python:3.10-slim

WORKDIR /bootstrap
COPY . /bootstrap
RUN pip3 --no-cache-dir install -r requirements.txt


ENTRYPOINT [ "python3", "./populate_db.py" ]