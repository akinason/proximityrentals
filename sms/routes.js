var express = require('express');
var router = express.Router();
var sms = require('./index');

router.post('/send', function(req, res, next) {
    to_number = req.body.to_number;
    msg = req.body.msg;
    res.send(sms.send(to_number, msg));
});

module.exports = router