Process // node에서 실행되는 모든 모듈들을 알 수가 있다.
process.version // 설치된 노드의 버전 확인
process.arch // 프로세서 아키텍처 정보
process.platform // 운영체제 플랫폼 정보 ex) win64
process.pid // 현재 프로세스의 아이디
process.uptime() // 프로세스가 시작된 후 흐른 시간. 단위 초
process.execPath // 노드가 있는 경로
process.cwd() // 현재 프로세스가 실행되는 위치 // 자주 사용 된다.
process.cpuUsage()// 현재 cpu 사용량

process.env // 환경변수 비밀키, 서드파티 앱 등 보관 용도, NODE_OPTIONS(노드 실행 옵션), UV_THREADPOOL_SIZE(스레드풀 개수) 등, 

process.nextTick // 이벤트 루프가 다른 콜백 함수들보다 nextTick의 콜백 함수를 우선적으로 처리한다.
// 즉, promise, nextTick은 우선순위가 높아 먼저 실행된다. (둘 끼리는 먼저 실행된게 먼저 실행됨)
// 나머지 콜백 함수들은 promise, nextTick이 실행되고 실행 된다.

process.exit(코드) //현재의 프로세스를 종료하고 싶을 때 사용한다.
//코드가 없거나 0이면 정상 종료, 이외의 코드는 비정상 종료를 의미한다.