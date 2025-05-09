
FROM lscr.io/linuxserver/code-server:latest

WORKDIR /config/workspace

RUN curl -s https://deb.nodesource.com/setup_18.x | sudo bash && sudo apt install nodejs -y


# FROM lscr.io/linuxserver/code-server
# RUN apt update && apt-get update && apt upgrade -y && apt-get upgrade -y
# RUN apt install -y curl
# RUN apt remove nodejs && apt remove libnode72
# RUN curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
# RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/nodesource-archive-keyring.gpg
# RUN echo "deb [signed-by=/usr/share/keyrings/nodesource-archive-keyring.gpg] https://deb.nodesource.com/node_18.x jammy main" | sudo tee /etc/apt/sources.list.d/nodesource.list
# RUN curl -s https://deb.nodesource.com/setup_18.x | sudo bash && sudo apt install nodejs -y
# RUN apt update && apt-get update && apt upgrade -y && apt-get upgrade -y
# RUN apt install nodejs -y