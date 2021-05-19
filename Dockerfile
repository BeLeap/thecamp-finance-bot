FROM python:3

COPY . .
RUN pip3 install -r requirements.txt
RUN python3 ./setup.py

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]