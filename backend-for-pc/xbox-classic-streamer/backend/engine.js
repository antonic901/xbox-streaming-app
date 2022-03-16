'use strict';

var logger = require('./utils/logger');
var torrentStream = require('torrent-stream');
var _ = require('lodash');
var net = require('net');

var BITTORRENT_PORT = 6881;
var tryPort = new Promise(function (resolve) {
  function findPort(port) {
    var s = net.createServer();
    s.on('error', function() {
      findPort(0);
    });

    s.listen(port, function() {
      var port = s.address().port;
      s.close(function() {
        resolve(port);
      });
    });
  }
  findPort(BITTORRENT_PORT);
});

module.exports = function (torrent, opts) {
  var engine = torrentStream(torrent, _.cloneDeep(opts));

  engine.once('verifying', function () {
    var totalPieces = engine.torrent.pieces.length;
    var verifiedPieces = 0;

    logger.log('NOTICE', 'verifying ' + engine.infoHash);
    engine.files.forEach(function (file, i) {
      logger.log('NOTICE', i + ' ' + file.name);
    });

    engine.on('verify', function () {
      if (++verifiedPieces === totalPieces) {
        engine.emit('finished');
        logger.log('NOTICE', 'finished ' + engine.infoHash);
      }
    });
  });

  engine.once('ready', function () {
    logger.log('NOTICE', 'ready ' + engine.infoHash);
    engine.ready = true;

    // select the largest file
    var file = engine.files.reduce(function (a, b) {
      return a.length > b.length ? a : b;
    });
    file.select();
  });

  engine.on('uninterested', function () {
    logger.log('NOTICE', 'uninterested ' + engine.infoHash);
  });

  engine.on('interested', function () {
    logger.log('NOTICE', 'interested ' + engine.infoHash);
  });

  engine.on('idle', function () {
    logger.log('NOTICE', 'idle ' + engine.infoHash);
  });

  engine.on('error', function (e) {
    logger.log('NOTICE', 'error ' + engine.infoHash + ': ' + e);
  });

  engine.once('destroyed', function () {
    logger.log('NOTICE', 'destroyed ' + engine.infoHash);
    engine.removeAllListeners();
  });

  tryPort.then(function (port) {
    engine.listen(port, function () {
      logger.log('NOTICE', 'listening ' + engine.infoHash + ' on port ' + engine.port);
    });
  });

  return engine;
};
