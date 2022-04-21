#!/usr/bin/env node
'use strict';

var logger = require('./utils/logger'),
  process = require('process'),
  network = require('./utils/network'),
  configuration = require('./configuration');

logger.create();
logger.log('NOTICE', 'Starting API...');

var STATIC_OPTIONS = { maxAge: 3600000 };

process.title = 'xbox-streaming-server';

var host = process.env.HOST || network.getHostAddress();
var port = process.env.PORT || 9006;

if (!configuration.readConfigurationFile()) {
  logger.log('NOTICE', 'Configuration file is not found. Creating one...');
  if (!configuration.writeConfigurationFile(configuration.createConfigurationFile(host, port))) {
    logger.log('ERROR', 'Error while creating configuration while. Maybe path is wrong?');
    process.exit(1);
  } else {
    logger.log('NOTICE', 'Configuration file is successfully created.');
  }
} else {
  logger.log('NOTICE', 'Configuration file is founded.');
}

var express = require('express'),
  http = require('http'),
  path = require('path'),
  serveStatic = require('serve-static'),
  socket = require('./socket'),
  api = require('./')
    .use(serveStatic(path.join(__dirname, '../dist'), STATIC_OPTIONS))
    .use(serveStatic(path.join(__dirname, '../.tmp'), STATIC_OPTIONS))
    .use(serveStatic(path.join(__dirname, '../frontend'), STATIC_OPTIONS));

var server = http.createServer(api);
socket(server);

server.listen(port, host).on('error', function (e) {
  if (e.code !== 'EADDRINUSE' && e.code !== 'EACCES') {
    throw e;
  }
  logger.log('ERROR', 'Port ' + port + ' is busy. Trying the next available port...');
  server.listen(++port);
}).on('listening', function () {
  logger.log('NOTICE', 'API is successfully started. Listening on http://' + host + ':' + port);
});

module.exports = {host, port}