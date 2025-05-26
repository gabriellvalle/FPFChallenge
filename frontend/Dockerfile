FROM node:18-alpine as build

WORKDIR /app
COPY . .
RUN npm install -g @angular/cli
RUN npm install 
RUN npm run build --prod

FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
