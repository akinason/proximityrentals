'use strict';
module.exports = (sequelize, DataTypes) => {
  const sms = sequelize.define('sms', {
    sender: {
      type: DataTypes.STRING,
      allowNull: false
    },
    number: {
      type:DataTypes.TEXT,
      allowNull: false
    },
    messageId: {
      type: DataTypes.STRING,
      allowNull: false
    },
    sentDate: {
      type: DataTypes.DATE,
      allowNull: false
    },
    message: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    status: {
      type: DataTypes.STRING,
      allowNull: true
    },

  }, {});
  sms.associate = function(models) {
    // associations can be defined here
  };
  return sms;
};