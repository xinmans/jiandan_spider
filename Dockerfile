FROM python:3.8.12-slim
LABEL title="jiandan photoes spider"
LABEL description="get pics from https://jandan.net/"
LABEL authors="xinmans"
ENV DOWNLOAD_CRON='1 0 * * *'
WORKDIR /app
COPY jiandan.py /app
COPY requirements.txt /app
VOLUME /data
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y tzdata \
    && apt-get install -y cron \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip \
    && pip install -r /app/requirements.txt
RUN echo "$DOWNLOAD_CRON /usr/local/bin/python /app/jiandan.py  >> /var/log/cron.log 2>&1" > /etc/cron.d/download-cron
RUN chmod +x /etc/cron.d/download-cron
RUN crontab /etc/cron.d/download-cron
RUN touch /var/log/cron.log
CMD python /app/jiandan.py && cron && tail -f /var/log/cron.log
