FROM node:18-slim
WORKDIR /data
COPY ./data /data
RUN npm i -g  next
RUN npm install
CMD ["npm", "run", "dev"]