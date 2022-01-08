FROM node:17-alpine3.14

WORKDIR /app

RUN npm install node-fetch@2
RUN npm install tmi.js

COPY client.js .

ENTRYPOINT ["node", "client.js"]
