//패키지 접근제어 2

package main

import (
	"fmt"
	checkUp "section4/lib" // alias를 줘서 체계적으로 사용 가능
	_ "section4/lib2"      // _를 사용하면 저장시 사용하지 않아도 지워지지 않는다.
)

func main() {
	//패키지 접근제어
	//별칭 사용
	//빈 식별자 사용

	fmt.Println("10보다 큰 수? : ", checkUp.CheckNum(11))
}
