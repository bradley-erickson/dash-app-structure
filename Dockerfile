FROM python:3.9-slim

WORKDIR /src

COPY requirements.txt /

RUN pip install -r /requirements.txt \
	&& rm -rf /root/.cache

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8085

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]
