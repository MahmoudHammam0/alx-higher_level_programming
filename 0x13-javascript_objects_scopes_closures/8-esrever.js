#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length / 2;
  for (let i = 0; i < len; i++) {
    const temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }
  return list;
};
