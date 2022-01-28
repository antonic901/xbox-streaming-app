#!/usr/bin/env node
'use strict';

var STATIC_OPTIONS = { maxAge: 3600000 };

var process = require('process');
process.title = 'peerflix-server';

var express = require('express'),
  http = require('http'),
  path = require('path'),
  serveStatic = require('serve-static'),
  socket = require('./socket'),
  api = require('./')
    .use(serveStatic(path.join(__dirname, '../dist'), STATIC_OPTIONS))
    .use(serveStatic(path.join(__dirname, '../.tmp'), STATIC_OPTIONS))
    .use(serveStatic(path.join(__dirname, '../app'), STATIC_OPTIONS));

var server = http.createServer(api);
socket(server);

function getHostAddress() {
  const os = require('os');
  const nets = os.networkInterfaces();
  const results = Object.create(null); // Or just '{}', an empty object
  var host = null;

  for (const name of Object.keys(nets)) {
      for (const net of nets[name]) {
          // Skip over non-IPv4 and internal (i.e. 127.0.0.1) addresses
          if (net.family === 'IPv4' && !net.internal) {
              if (!results[name]) {
                  results[name] = [];
              }
              results[name].push(net.address);
              host = net.address;
          }
      }
  }
  return host;
};

var host = process.env.HOST || getHostAddress();
var port = process.env.PORT || 9005;

server.listen(port, host).on('error', function (e) {
  if (e.code !== 'EADDRINUSE' && e.code !== 'EACCES') {
    throw e;
  }
  console.error('Port ' + port + ' is busy. Trying the next available port...');
  server.listen(++port);
}).on('listening', function () {
  console.log('Listening on http://' + host + ':' + port);
});