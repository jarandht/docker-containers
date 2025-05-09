FROM lscr.io/linuxserver/code-server
RUN apt update && apt-get update && apt upgrade -y && apt-get upgrade -y
RUN apt install -y curl && apt install nano -y
RUN curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
RUN apt install -y npm