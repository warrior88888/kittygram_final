FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM alpine:3.19
WORKDIR /app
COPY --from=build /app/build /app/build

CMD ["sh", "-c", "cp -r /app/build/. /frontend_static/"]