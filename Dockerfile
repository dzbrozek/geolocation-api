FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV COLUMNS=80

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user \
  && adduser --disabled-password --gecos "" --uid $USER_ID --gid $GROUP_ID user

COPY geolocationapi/requirements.txt /app/requirements.txt
COPY entrypoint /app/entrypoint/

WORKDIR /app/geolocationapi

RUN pip install -r /app/requirements.txt --no-cache-dir \
    && apt-get update \
    && apt-get install -y \
    vim=2:8.1.0875-5 \
    postgresql-client=11+200+deb10u4 \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER user

ENTRYPOINT ["/app/entrypoint/entrypoint.sh"]
