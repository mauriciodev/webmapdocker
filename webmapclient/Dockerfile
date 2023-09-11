FROM node:20
WORKDIR /usr/src/app

COPY . .

RUN npm install
# If you are building your code for production
# RUN npm ci --omit=dev

EXPOSE 8001
CMD [ "npm", "start" ]
