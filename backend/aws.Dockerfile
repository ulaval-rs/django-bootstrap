FROM python:3.9-slim

WORKDIR /usr/src

RUN apt-get update \
    && apt-get install -y \
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

# Tell uWSGI where to find your wsgi file (change this):
ENV UWSGI_WSGI_FILE=api/wsgi.py  \
    UWSGI_HTTP=:80 \
    UWSGI_MASTER=1 \
    UWSGI_HTTP_AUTO_CHUNKED=1 \
    UWSGI_HTTP_KEEPALIVE=1 \
    UWSGI_LAZY_APPS=1 \
    UWSGI_WSGI_ENV_BEHAVIOR=holy \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=4 \
    UWSGI_STATIC_MAP="/static/=/usr/static/" \
    UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000" \
    REPO_SHA=$REPO_SHA

# Start server
CMD ["uwsgi", "--show-config"]
