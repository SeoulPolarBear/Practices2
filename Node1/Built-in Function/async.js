const fs = require('fs');

const readme = async() =>{
    let data1 = await fs.readFile("./readme.txt");
    console.log('1번', data1.toString())
    let data2 = await fs.readFile("./readme.txt");
    console.log('1번', data2.toString())
    let data3 = await fs.readFile("./readme.txt");
    console.log('1번', data3.toString())
    let data4 = await fs.readFile("./readme.txt");
    console.log('1번', data4.toString())
}

fs.readFile("./readme.txt", (err, data) => {
  if (err) {
    throw err;
  }
  console.log("1번", data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
});

fs.readFile("./readme.txt", (err, data) => {
    if (err) {
      throw err;
    }
    console.log("2번", data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
  });
  
fs.readFile("./readme.txt", (err, data) => {
    if (err) {
      throw err;
    }
    console.log("3번", data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
  });
  
fs.readFile("./readme.txt", (err, data) => {
    if (err) {
      throw err;
    }
    console.log("4번", data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
  });
    
//   3번 node.js practice
//   1번 node.js practice
//   2번 node.js practice
//   4번 node.js practice
// 비동기여서 한번에 실행되므로 random이 될 수 있다.