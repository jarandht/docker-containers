FROM ubuntu
RUN apt-get update && apt-get upgrade -y
RUN cd /home
RUN apt install curl -y
RUN apt install gnupg -y
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list && apt update && apt install ngrok
RUN ngrok config add-authtoken "token"