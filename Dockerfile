FROM python:3

RUN apt update
RUN apt install cron -y
RUN cp -p /usr/share/zoneinfo/Asia/Seoul /etc/localtime

COPY . .
RUN pip3 install -r requirements.txt
RUN python3 ./setup.py

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]