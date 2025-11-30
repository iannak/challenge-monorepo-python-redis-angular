FROM node:20 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
	RUN npm run build -- --output-path=dist/frontend/browser

# Serve Angular app directly with Node.js
EXPOSE 4200
	CMD ["npx", "http-server", "dist/frontend/browser", "-p", "4200", "-c-1"]
