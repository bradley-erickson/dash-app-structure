FROM python:3.11
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app/src
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:server", "-k", "gevent"]
