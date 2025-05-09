FROM ubuntu
RUN apt-get update && apt-get upgrade -y
RUN cd /home
RUN apt install curl -y
RUN apt install gnupg -y
RUN curl -SsL https://playit-cloud.github.io/ppa/key.gpg | apt-key add -
RUN curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list
RUN apt update -y
RUN apt install playit -y
RUN apt install systemctl -y