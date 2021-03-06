'use strict';

var stats = require('./stats'),
  logger = require('./utils/logger');

module.exports = function (server) {
  var io = require('socket.io').listen(server),
    _ = require('lodash'),
    progress = require('./progressbar'),
    store = require('./store');

  io.sockets.on('connection', function (socket) {
    socket.on('stop', function(infoHash, index) {
      logger.log('NOTICE', 'stopping ' + infoHash);
      var torrent = store.get(infoHash);
      if(index >= 0 && index < torrent.files.length) {
        torrent.files[index].deselect();
      } else {
        torrent.files.forEach(function (f) {
          f.deselect();
        });
      }
    });
    socket.on('start', function(infoHash, index) {
      logger.log('NOTICE', 'starting ' + infoHash);
      var torrent = store.get(infoHash);
      if(index >= 0 && index < torrent.files.length) {
        torrent.files[index].select();
      } else {
        torrent.files.forEach(function (f) {
          f.select();
        });
      }
    });
    socket.on('pause', function (infoHash) {
      logger.log('NOTICE', 'pausing ' + infoHash);
      var torrent = store.get(infoHash);
      if (torrent && torrent.swarm) {
        torrent.swarm.pause();
      }
    });
    socket.on('resume', function (infoHash) {
      logger.log('NOTICE', 'resuming ' + infoHash);
      var torrent = store.get(infoHash);
      if (torrent && torrent.swarm) {
        torrent.swarm.resume();
      }
    });
    socket.on('select', function (infoHash, file) {
      if (typeof file === 'number') {
        logger.log('NOTICE', 'selected ' + infoHash + '/' + file);
      } else {
        logger.log('NOTICE', 'selected ' + infoHash);
      }
      var torrent = store.get(infoHash);
      if (torrent && torrent.files) {
        if (typeof file === 'number') {
          file = torrent.files[file];
          file.select();
        } else {
          torrent.files.forEach(function (f) {
            f.select();
          });
        }
      }
    });
    socket.on('deselect', function (infoHash, file) {
      if (typeof file === 'number') {
        logger.log('NOTICE', 'deselected ' + infoHash + '/' + file);
      } else {
        logger.log('NOTICE', 'deselected ' + infoHash);
      }
      var torrent = store.get(infoHash);
      if (torrent && torrent.files) {
        if (typeof file === 'number') {
          file = torrent.files[file];
          file.deselect();
        } else {
          torrent.files.forEach(function (f) {
            f.deselect();
          });
        }
      }
    });
  });

  store.on('torrent', function (infoHash, torrent) {
    function listen() {
      var notifyProgress = _.throttle(function () {
        io.sockets.emit('download', infoHash, progress(torrent.bitfield.buffer));
      }, 1000, { trailing: false });

      var notifySelection = _.throttle(function () {
        var pieceLength = torrent.torrent.pieceLength;
        io.sockets.emit('selection', infoHash, torrent.files.map(function (f) {
          // jshint -W016
          var start = f.offset / pieceLength | 0;
          var end = (f.offset + f.length - 1) / pieceLength | 0;
          return torrent.selection.some(function (s) {
            return s.from <= start && s.to >= end;
          });
        }));
      }, 2000, { trailing: false });

      io.sockets.emit('verifying', infoHash, stats(torrent));

      torrent.once('ready', function () {
        io.sockets.emit('ready', infoHash, stats(torrent));
      });

      torrent.on('uninterested', function () {
        io.sockets.emit('uninterested', infoHash);
        notifySelection();
      });

      torrent.on('interested', function () {
        io.sockets.emit('interested', infoHash);
        notifySelection();
      });

      var interval = setInterval(function () {
        io.sockets.emit('stats', infoHash, stats(torrent));
        notifySelection();
      }, 1000);

      torrent.on('verify', notifyProgress);

      torrent.on('finished', function () {
        io.sockets.emit('finished', infoHash);
        notifySelection();
        notifyProgress();
      });

      torrent.once('destroyed', function () {
        clearInterval(interval);
        io.sockets.emit('destroyed', infoHash);
      });
    }

    if (torrent.torrent) {
      listen();
    } else {
      torrent.once('verifying', listen);
    }
  });
};
