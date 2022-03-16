'use strict';

let path = "./";
let name = "configuration.json";

const file = require('./utils/file');

function readConfigurationFile() {
    return JSON.parse(file.read(path,name));
  }

function writeConfigurationFile(data) {
    return file.write(path, name, data);
}

function createConfigurationFile(host, port) {
    let configuration = {
        PC: {
            IP_ADDRESS: host,
            PORT: port
        },
        XBOX: {
            IP_ADDRESS: '0.0.0.0',
            PORT: '80'
        }
    };
    let data = JSON.stringify(configuration);
    return data;
}

module.exports = {
    readConfigurationFile,
    writeConfigurationFile,
    createConfigurationFile
};