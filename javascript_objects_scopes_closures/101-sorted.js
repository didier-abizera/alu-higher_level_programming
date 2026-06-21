#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
}
console.log(newDict);
