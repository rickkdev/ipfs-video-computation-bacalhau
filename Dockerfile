# FROM python:3.11
# COPY . /app
# WORKDIR /app
# RUN pip3 install pipenv
# RUN pip3 install opencv-python
# RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

# # RUN pipenv install --system --deploy --ignore-pipfile
# ENTRYPOINT [ "python" ]
# CMD [ "compute.py" ]



FROM python:slim

RUN apt-get update && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /project

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install pipenv
RUN pip3 install opencv-python

# COPY ./requirements.txt /project


COPY ./main.py /project

CMD ["python","main.py"]