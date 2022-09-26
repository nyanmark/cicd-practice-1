FROM node:16.17.0 as build 

WORKDIR /app
COPY ./package.json . 
COPY ./package-lock.json . 
COPY ./.env .
RUN npm install 

COPY ./public ./public/ 
COPY ./src ./src/ 
COPY ./.env .
RUN npm run build 

FROM nginx:1.22-alpine
RUN apk add --update nodejs npm

COPY --from=build /app/node_modules/cra-envs/package.json ./cra-envs-package.json
RUN npm i -g cra-envs@`node -e 'console.log(require("./cra-envs-package.json")["version"])'`

WORKDIR /usr/share/nginx
COPY --from=build /app/build ./html 
COPY --from=build /app/.env .
COPY --from=build /app/package.json .
COPY --from=build /app/public/index.html ./public/

EXPOSE 80 
ENTRYPOINT sh -c "npx embed-environnement-variables && nginx -g 'daemon off;'"