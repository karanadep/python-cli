FROM python:3
MAINTAINER Karankumar Adep <karan.adep@gmail.com>

COPY main.py main.py
COPY apiAlerts.py apiAlerts.py

CMD ["./main.py"]