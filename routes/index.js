var express = require('express');
var router = express.Router();
var userRouter = require('../user/router');
var smsRouter = require('../sms/routes');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.use('/user', userRouter);
router.use('/sms', smsRouter);

module.exports = router;