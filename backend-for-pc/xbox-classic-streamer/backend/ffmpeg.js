'use strict';

var path = require('path'),
  fs = require('fs'),
  pump = require('pump');

module.exports = function (req, res, torrent, file) {
  var param = req.query.ffmpeg,
    ffmpeg = require('fluent-ffmpeg');

  function probe() {
    var filePath = path.join(torrent.path, file.path);
    fs.exists(filePath, function (exists) {
      if (!exists) {
        return res.status(404).send('File doesn`t exist.');
      }
      return ffmpeg.ffprobe(filePath, function (err, metadata) {
        if (err) {
          console.error(err);
          return res.status(500).send(err.toString());
        }
        res.send(metadata);
      });
    });
  }

  function remux() {
    res.type('video/webm');

    var filePath = path.join(torrent.path, file.path);

    var command = ffmpeg(file.createReadStream())
      .audioCodec('aac')
      .videoCodec('mpeg4')
      .videoBitrate(3000)
      .outputOptions([
        //'-threads 2',
        '-scodec copy',
        '-maxrate 5000k',
        '-bufsize 4096k',
        '-s 1280x720',
        '-ac 2',
        '-q:a 5'
        // '-deadline realtime',
        // '-error-resilient 1'
      ])
      .format('matroska')
      .on('start', function (cmd) {
        console.log(cmd);
      })
      .on('error', function (err) {
        console.error(err);
      });
    pump(command, res);
  }

  switch (param) {
    case 'probe':
      return probe();
    case 'remux':
      return remux();
    default:
      res.status(501).send('Not supported.');
  }
};
