FROM node:YOUR NODE VERSION
WORKDIR /data
COPY package*.json ./
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
ENTRYPOINT ["/startup.sh"]
