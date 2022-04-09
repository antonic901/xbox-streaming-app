'use strict';

const { urlencoded } = require('body-parser');

var rangeParser = require('range-parser'),
  pump = require('pump'),
  _ = require('lodash'),
  express = require('express'),
  morgan = require('morgan'),
  bodyParser = require('body-parser'),
  multipart = require('connect-multiparty'),
  fs = require('fs'),
  archiver = require('archiver'),
  store = require('./store'),
  progress = require('./progressbar'),
  stats = require('./stats'),
  TorrentSearchApi = require('torrent-search-api'),
  configuration = require('./configuration'),
  api = express(),
  axios = require('axios'),
  logger = require('./utils/logger'),
  fileParser = require('episode-parser'),
  path = require('path');

let enableProviders = ['1337x', 'Rarbg', 'ThePirateBay', 'Yts'];
logger.log('NOTICE', 'Enabling providers: ' + enableProviders);
enableProviders.forEach(provider => {
  TorrentSearchApi.enableProvider(provider);
  logger.log('NOTICE', TorrentSearchApi.isProviderActive(provider) ? provider + ' is active.'  : provider + ' is not active.')
});

api.use(bodyParser.json())
api.use(morgan('dev'));
api.use(function (req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'OPTIONS, POST, GET, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

function serialize(torrent) {
  if (!torrent.torrent) {
    return { infoHash: torrent.infoHash };
  }
  var pieceLength = torrent.torrent.pieceLength;

  return {
    infoHash: torrent.infoHash,
    name: torrent.torrent.name,
    length: torrent.torrent.length,
    interested: torrent.amInterested,
    ready: torrent.ready,
    files: torrent.files.map(function (f) {
      var start = f.offset / pieceLength | 0;
      var end = (f.offset + f.length - 1) / pieceLength | 0;

      return {
        name: f.name,
        path: f.path,
        link: '/torrents/' + torrent.infoHash + '/files/' + encodeURIComponent(f.path),
        length: f.length,
        offset: f.offset,
        selected: torrent.selection.some(function (s) {
          return s.from <= start && s.to >= end;
        })
      };
    }),
    progress: progress(torrent.bitfield.buffer),
    stats: stats(torrent)
  };
}

function findTorrent(req, res, next) {
  var torrent = req.torrent = store.get(req.params.infoHash);
  if (!torrent) {
    return res.sendStatus(404);
  }
  next();
}

api.get('/configuration', function(req, res) {
  res.send(configuration.readConfigurationFile());
});

api.post('/configuration', function(req, res){
  if(configuration.writeConfigurationFile(JSON.stringify(req.body))) res.status(200).send("Updated configuration file.");
  else res.status(404).send("Path is not found.");
});

api.get('/torrents', function (req, res) {
  res.send(store.list().map(serialize));
});

api.post('/torrents', function (req, res) {
  store.add(req.body.link, function (err, infoHash) {
    if (err) {
      logger.log('ERROR', err);
      res.status(500).send(err);
    } else {
      res.send({ infoHash: infoHash });
    }
  });
});

api.post('/upload', multipart(), function (req, res) {
  var file = req.files && req.files.file;
  if (!file) {
    return res.status(500).send('file is missing');
  }
  store.add(file.path, function (err, infoHash) {
    if (err) {
      logger.log('ERROR', err);
      res.status(500).send(err);
    } else {
      res.send({ infoHash: infoHash });
    }
    fs.unlink(file.path, function (err) {
      if (err) {
        logger.log('ERROR', err);
      }
    });
  });
});

api.get('/torrents/:infoHash', findTorrent, function (req, res) {
  if(!req.torrent.torrent) {
    res.status(304).send(serialize(req.torrent));
  } else {
    res.send(serialize(req.torrent));
  }
});

/*
>> Accept:
        body: 
            episode
            season
        path: 
            infoHash -> torrent hash
        query: empty
    Used for:
        Finds file/episode of interest and select it.
        Deselect all other files/episodes in this torrent.
*/
api.post('/torrents/:infoHash/episode', findTorrent, function(req, res) {
    var season = req.body.season,
        episode = req.body.episode,
        path = null;
    req.torrent.files.forEach(file => {
        var result = fileParser(file.name)
        if (!result) {
            file.deselect();
        }
        else if(result.episode == episode && result.season == season) {
            logger.log('NOTICE', 'selecting ' + file.name)
            path = file.path;
            file.select();
        }
        else {
            file.deselect();
        }
    })
    res.send(encodeURI(path));
});

/*
>> Accept:
        body: empty
        path: 
            infoHash -> torrent hash
        query: empty
    Used for:
        Finds largest file (which is movie) and select it.
        Deselect all other files.
*/
api.post('/torrents/:infoHash/movie', findTorrent, function(req, res) {
    var files =  _.orderBy(req.torrent.files, ['length'], ['desc']),
        path = null;
    for(var i = 0; i < files.length; i++) {
        if (i == 0) {
            logger.log('NOTICE', 'selecting ' + files[i].name);
            path = files[i].path;
            files[i].select();
        } else {
            files[i].deselect();
        }
    }
    res.send(encodeURI(path));
});

api.get('/torrents/:infoHash/file', findTorrent, function (req, res) {
    var filePath = path.join(req.torrent.path, decodeURI(req.body.filePath));
    console.log(filePath);
    if(fs.existsSync(filePath)) {
        var fileSizeInMegabytes = fs.statSync(filePath).size / (1024*1024);
        res.send(fileSizeInMegabytes.toString());
    } else {
        res.sendStatus(404);
    }
});

api.post('/torrents/:infoHash/start/:index?', findTorrent, function (req, res) {
  var index = parseInt(req.params.index);
  if (index >= 0 && index < req.torrent.files.length) {
    req.torrent.files[index].select();
  } else {
    req.torrent.files.forEach(function (f) {
      f.select();
    });
  }
  res.sendStatus(200);
});

api.post('/torrents/:infoHash/stop/:index?', findTorrent, function (req, res) {
  var index = parseInt(req.params.index);
  if (index >= 0 && index < req.torrent.files.length) {
    req.torrent.files[index].deselect();
  } else {
    req.torrent.files.forEach(function (f) {
      f.deselect();
    });
  }
  res.sendStatus(200);
});

api.post('/torrents/:infoHash/pause', findTorrent, function (req, res) {
  req.torrent.swarm.pause();
  res.sendStatus(200);
});

api.post('/torrents/:infoHash/resume', findTorrent, function (req, res) {
  req.torrent.swarm.resume();
  res.sendStatus(200);
});

api.delete('/torrents/:infoHash', findTorrent, function (req, res) {
  store.remove(req.torrent.infoHash);
  res.sendStatus(200);
});

api.get('/torrents/:infoHash/stats', findTorrent, function (req, res) {
  res.send(stats(req.torrent));
});

api.get('/torrents/:infoHash/files', findTorrent, function (req, res) {
  var torrent = req.torrent;
  var proto = req.get('x-forwarded-proto') || req.protocol;
  var host = req.get('x-forwarded-host') || req.get('host');
  res.setHeader('Content-Type', 'application/x-mpegurl; charset=utf-8');
  res.attachment(torrent.torrent.name + '.m3u');
  res.send('#EXTM3U\n' + torrent.files.map(function (f) {
      return '#EXTINF:-1,' + f.path + '\n' +
        proto + '://' + host + '/torrents/' + torrent.infoHash + '/files/' + encodeURIComponent(f.path);
    }).join('\n'));
});

api.all('/torrents/:infoHash/files/:path([^"]+)', findTorrent, function (req, res) {
  var torrent = req.torrent, file = _.find(torrent.files, { path: req.params.path });

  console.log(req.params.path);

  if (!file) {
    return res.sendStatus(404);
  }

  if (typeof req.query.ffmpeg !== 'undefined') {
    return require('./ffmpeg')(req, res, torrent, file);
  }

  var range = req.headers.range;
  logger.log('NOTICE', 'Range: ' + range)
  range = range && rangeParser(file.length, range)[0];
  logger.log('NOTICE', 'Range after parsing: ' + JSON.stringify(range))
  res.setHeader('Accept-Ranges', 'bytes');
  res.type(file.name);
  req.connection.setTimeout(3600000);

  if (!range) {
    res.setHeader('Content-Length', file.length);
    if (req.method === 'HEAD') {
      return res.end();
    }
    return pump(file.createReadStream(), res);
  }

  res.statusCode = 206;
  res.setHeader('Content-Length', range.end - range.start + 1);
  res.setHeader('Content-Range', 'bytes ' + range.start + '-' + range.end + '/' + file.length);

  if (req.method === 'HEAD') {
    return res.end();
  }
  pump(file.createReadStream(range), res);
});

/*
>> Body:
        path (String) -> relative path to file
        end (size in Bytes) -> tell us how much tu buffer from end of file

    Path:
        infoHash (String) -> id of torrent

    Query: None

    Purpose:
        Says torrent-stream engine to download last "end" bytes of file (file.length - end <-> file.length)
*/
api.get('/torrents/:infoHash/moov-atom', findTorrent, function (req, res) {
    var torrent = req.torrent, file = _.find(torrent.files, { path: decodeURI(req.body.path) });
    file.createReadStream({
        start: file.length - req.body.end,
        end: file.length
    })
    res.sendStatus(200);
});

api.get('/torrents/:infoHash/archive', findTorrent, function (req, res) {
  var torrent = req.torrent;

  res.attachment(torrent.torrent.name + '.zip');
  req.connection.setTimeout(3600000);

  var archive = archiver('zip');
  archive.on('warning', function (err) {
    logger.log('ERROR', err);
  });
  archive.on('error', function (err) {
    throw err;
  });

  pump(archive, res);

  torrent.files.forEach(function (f) {
    archive.append(f.createReadStream(), { name: f.path });
  });
  archive.finalize();
});

api.get('/search/:query/:category', async function (req, res) {
  var query = req.params.query;
  var category = req.params.category;
  const torrents = await TorrentSearchApi.search(query, category, 20);
  res.send(torrents)
});

api.get('/magnet', async function (req, res) {
  var torrent = req.body.torrent;
  const magnet = await TorrentSearchApi.getMagnet(torrent);
  res.send(magnet)
});

module.exports = api;