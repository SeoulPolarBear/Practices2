// switch문 2
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	//예제1 // case도 && 같은 논리 연산자도 사용할 수 있다.
	rand.Seed(time.Now().UnixNano())
	switch i := rand.Intn(100); { // 0~100 값을 랜덤으로 가져오겠다.
	case i >= 50 && i < 100:
		fmt.Println("i -> ", i, " 50이상 100 미만")
	case i >= 25 && i < 50:
		fmt.Println("i -> ", i, " 25이상 50 미만")
	default:
		fmt.Println("i -> ", i, " 기본값")
	}

}
