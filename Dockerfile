FROM python:3.10
RUN set -xe

RUN apt-get update && apt-get install -y cron

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab \
    && crontab /etc/cron.d/crontab

WORKDIR /app
COPY /usagovjobs ./usagovjobs/
COPY /tests ./tests/
RUN mkdir reports
COPY pyproject.toml poetry.lock Makefile .env runner.sh ./

RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry --version
RUN poetry install
RUN make test

RUN pip install poetry

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh