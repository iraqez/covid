# install latest ubuntu & python
FROM ubuntu:latest
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    python3-pip python3-setuptools python3-dev && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# create djangoapp directory inside docker container & install django
RUN mkdir /covidsapp
COPY . /covidsapp
WORKDIR /covidsapp
RUN pip3 install -r requirements.txt

#set permission for our bash file
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]

