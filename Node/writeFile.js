const fs = require('fs').promises; //promises는 fs를 promise로도 사용할 수 있게 해준다.


fs.writeFile("./writeme.txt", 'node.js practice write')
  .then(() => {
    return fs.readFile('./writeme.txt');
  })//tnen을 chain 형태로 사용 이때 2번째 then은 () => 의 then이다.
  .then((data) =>{
    console.log(data.toString())
  })
  .catch((err) => {
      throw err;
  });
    