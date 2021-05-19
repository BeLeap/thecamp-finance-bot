FROM python:3

COPY . .
RUN apt update
RUN apt install cron -y
RUN pip3 install -r requirements.txt
RUN python3 ./setup.py

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]