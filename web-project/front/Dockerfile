FROM node:18-slim

WORKDIR /front
COPY package*.json ./
RUN npm install
COPY . .

CMD ["npm", "run", "dev"]