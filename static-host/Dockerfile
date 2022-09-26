FROM node:16.17.0 as build 

RUN npm install -g gulp-cli

WORKDIR /app
COPY ./package.json . 
COPY ./package-lock.json . 
RUN npm install 

COPY ./src ./src/ 
COPY ./gulpfile.js .
RUN gulp

FROM nginx:1.22-alpine

WORKDIR /usr/share/nginx
RUN rm /usr/share/nginx/html/index.html
COPY --from=build /app/build ./html 

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]