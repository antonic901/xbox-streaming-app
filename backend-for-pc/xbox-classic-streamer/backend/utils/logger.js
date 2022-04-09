'use strict';

let path = './';
let name = 'log.txt';

let file  = require('./file');

function log(type, message) {
    var log = new Date().toLocaleString() + " " + type  + ": " + message + "\n";
    file.append(path, name, log);
    if (type === "ERROR") {
        console.error(message);
    } else {
        console.log(message);
    }
}

function create() {
    if(file.exists(path, name)) {
        file.rename(path, name, "log.old.txt")
    }
    file.write(path, name, "");
}

function read() {
    return file.read(path, name);
}

module.exports = {
    log,
    create,
    read
};