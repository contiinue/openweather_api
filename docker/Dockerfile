FROM python:3.10

ARG USER_ID=2000
ARG GROUP_ID=2000


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install \
    && python -m pip install --upgrade pip

WORKDIR /app

COPY . app/

RUN pip install -r app/docker/requirements.txt

ENTRYPOINT ["sh", "app/docker/server_run.sh"]






