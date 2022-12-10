const fs = require('fs').promises; //promises는 fs를 promise로도 사용할 수 있게 해준다.
// callback형식을 띈다 즉, 실패와 성공이 나눠진다.
// fs.readFile('./readme.txt', (err, data) => {
//     if(err){
//         throw err;
//     }
//     console.log(data); // 사람이 못 읽는 상태
//     console.log(data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
// });

fs.readFile("./readme.txt")
  .then(() => {
    console.log(data); // 사람이 못 읽는 상태
    console.log(data.toString()); // toString을 해야지 사람이 읽을 수 있는 상태로 바뀌게 된다.
  })
  .catch((err) => {
      throw err;
  });
    