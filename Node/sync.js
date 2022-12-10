const fs = require('fs');

let data = fs.readFile("./readme.txt")
  console.log("1번", data.toString());

  let data2 = fs.readFile("./readme.txt")
  console.log("2번", data2.toString());

  let data3 = fs.readFile("./readme.txt")
  console.log("3번", data3.toString());

  let data4 = fs.readFile("./readme.txt")
  console.log("4번", data4.toString());



    
//   1번 node.js practice
//   2번 node.js practice
//   3번 node.js practice
//   4번 node.js practice
// 비동기여서 한번에 실행되므로 random이 될 수 있다.