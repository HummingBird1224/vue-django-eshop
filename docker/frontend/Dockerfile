FROM ruby:3.0.0-alpine

RUN apk add --no-cache nodejs nodejs-npm yarn bash docker openrc

COPY ./src/frontend/package*.json ./
COPY ./src/frontend/yarn.lock ./
COPY ./src/frontend/webpack.config.js ./
COPY ./src/frontend/webpack-stats.json ./

RUN yarn install

WORKDIR /suez/src/frontend
CMD yarn watch
