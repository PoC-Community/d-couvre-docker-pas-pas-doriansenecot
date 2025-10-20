FROM node:12-alpine

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install

COPY . .

ARG PORT=8080
ENV PORT=$PORT
EXPOSE $PORT

CMD ["npm", "start"]
