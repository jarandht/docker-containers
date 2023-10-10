FROM node:18-slim
WORKDIR /data
COPY package*.json ./
COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/startup.sh"]