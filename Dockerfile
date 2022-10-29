FROM python:slim

RUN apt-get update && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /project

COPY ./main.py /project

RUN pip3 install opencv-python

CMD ["python","main.py"]