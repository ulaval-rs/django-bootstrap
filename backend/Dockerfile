FROM python:3.8-slim

WORKDIR /usr/src

RUN apt-get update \
    && apt-get install -y \
    gcc \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists

EXPOSE 8080

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

COPY . /usr/src

RUN python -m compileall .

RUN chmod -R 775 /usr/src
RUN chown -R 1000:root /usr/src
USER 1000

RUN chmod +x ./entrypoint.sh

CMD gunicorn --bind 0.0.0.0:8080 csf.wsgi
