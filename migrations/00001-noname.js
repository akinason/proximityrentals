'use strict';

var Sequelize = require('sequelize');

/**
 * Actions summary:
 *
 * createTable "sms", deps: []
 *
 **/

var info = {
    "revision": 1,
    "name": "noname",
    "created": "2018-11-18T14:44:37.875Z",
    "comment": ""
};

var migrationCommands = [{
    fn: "createTable",
    params: [
        "sms",
        {
            "id": {
                "type": Sequelize.INTEGER,
                "autoIncrement": true,
                "primaryKey": true,
                "allowNull": false
            },
            "sender": {
                "type": Sequelize.STRING,
                "allowNull": false
            },
            "number": {
                "type": Sequelize.TEXT,
                "allowNull": false
            },
            "messageId": {
                "type": Sequelize.STRING,
                "allowNull": false
            },
            "sentDate": {
                "type": Sequelize.DATE,
                "allowNull": false
            },
            "message": {
                "type": Sequelize.TEXT,
                "allowNull": false
            },
            "status": {
                "type": Sequelize.STRING,
                "allowNull": true
            },
            "createdAt": {
                "type": Sequelize.DATE,
                "allowNull": false
            },
            "updatedAt": {
                "type": Sequelize.DATE,
                "allowNull": false
            }
        },
        {}
    ]
}];

var rollbackCommands = [{
    fn: "dropTable",
    params: ["sms"]
}];

module.exports = {
    pos: 0,
    up: function(queryInterface, Sequelize)
    {
        var index = this.pos;
        return new Promise(function(resolve, reject) {
            function next() {
                if (index < migrationCommands.length)
                {
                    let command = migrationCommands[index];
                    console.log("[#"+index+"] execute: " + command.fn);
                    index++;
                    queryInterface[command.fn].apply(queryInterface, command.params).then(next, reject);
                }
                else
                    resolve();
            }
            next();
        });
    },
    down: function(queryInterface, Sequelize)
    {
        var index = this.pos;
        return new Promise(function(resolve, reject) {
            function next() {
                if (index < rollbackCommands.length)
                {
                    let command = rollbackCommands[index];
                    console.log("[#"+index+"] execute: " + command.fn);
                    index++;
                    queryInterface[command.fn].apply(queryInterface, command.params).then(next, reject);
                }
                else
                    resolve();
            }
            next();
        });
    },
    info: info
};
