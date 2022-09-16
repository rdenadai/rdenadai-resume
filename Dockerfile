FROM python:3.10.7-slim-buster

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

WORKDIR /code
COPY ./entrypoint.sh .
COPY ./requirements.txt .

RUN apt-get install -y tzdata

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=C.UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    LC_CTYPE=C.UTF-8 LC_MESSAGES=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

RUN apt-get update && \ 
    # Timezone
    apt-get install -y tzdata && \ 
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && \
    apt install -y --no-install-recommends dumb-init  make build-essential \
    libpq-dev gcc libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pip setuptools==57.5.0 --upgrade && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["dumb-init", "--"]
CMD ["tail", "-f", "/dev/null"]