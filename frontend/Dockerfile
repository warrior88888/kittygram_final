FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM alpine
WORKDIR /app
COPY --from=build /app/build /app/build

CMD ["cp", "-r", "/app/build/.", "/frontend_static/"]