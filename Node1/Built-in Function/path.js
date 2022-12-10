const path = require('path')
//path 장점

// window : \ or \ ex) user\User\...
// linux : / ex) user/User/...
// path 모듈을 사용하면 이런 것들을 전부 잡아서 처리해줘서 신경 쓸 필요가 없다.

console.log(path.join(__dirname,'..','var.js')); // 절대경로를 우대해준다.

console.log(path.resolve(__dirname,'..','./var.js')); // 앞에 절대 경로가 있으면 절대경로를 무시한다.