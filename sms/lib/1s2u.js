const env = process.env.NODE_ENV || 'development';
const request = require('request');
const fs = require('fs');
const path = require('path');

const config = require(path.join(__dirname, "../../config/sms.json"))[env];
const smsModel = require('../../models').sms;

const Log = require('log')
    , stream = fs.createWriteStream(path.join(__dirname, "../../logs/sms.log"), {flags: 'a'})
    , log = new Log('info', stream)

class SMS {
    constructor(options={}){
        this.options = options
    }
}   

/*
    Formats sms sending following 1s2u.com API documentation.
*/
SMS.prototype.send = function(to_number, msg) {
    // Remove the leading "+" and any spacing in the number.
    var mno = String(to_number).replace(" ", "").replace("+", "").replace("-", "");
    var url = config._1s2u.url;
    var username = config._1s2u.username;
    var password = config._1s2u.password;
    var sid = config._1s2u.sender || "";
    var fl = 0;
    var mt = 0;
    var ipcl = "127.0.0.1";
    var content = "";
    var statusCode = "";
    var params = {
        username:username, password:password, msg:msg, mno:mno,
        Sid:sid, fl:fl, mt:mt, ipcl:ipcl
    };

    request.get({url:url, qs:params}, function(error, response, body) {
      
        if (error) {
            return 00
        }

        msgId = body
        smsModel
            .create({sender:sid, number:mno, messageId:msgId, sentDate:new Date(), message:msg, status:"submitted" })
            .catch(err => log.warning(err))
        
        return msgId
    });
}



module.exports = SMS
