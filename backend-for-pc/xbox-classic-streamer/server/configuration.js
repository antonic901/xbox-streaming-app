'use strict';
const fs = require('fs');

function readConfigurationFile(path, file_name) {
    if (!fs.existsSync(path + file_name)) {
      return null;
    }
    let data = fs.readFileSync(path + file_name);
    let configuration = JSON.parse(data);
    return configuration;
  }

function writeConfigurationFile(path, data, file_name) {
    if (!fs.existsSync(path)) {
        console.log("Path: '" + path + "' is not valid.");
        return null;
    }
    fs.writeFileSync(path + file_name, data);
    return data;
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