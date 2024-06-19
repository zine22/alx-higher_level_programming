#!/usr/bin/node
exports.addMeMaybe = function (numValue, func) {
  func(++numValue);
};
