FROM node:16.17.0 as build 
ARG API_URL 

WORKDIR /app
COPY ./package.json . 
COPY ./package-lock.json . 
RUN npm install 

COPY ./public ./public/ 
COPY ./src ./src/ 
RUN REACT_APP_API_URL=${API_URL} \ 
  npm run build 

FROM nginx:1.22-alpine 
COPY --from=build /app/build /usr/share/nginx/html 
EXPOSE 80 
CMD ["nginx", "-g", "daemon off;"]