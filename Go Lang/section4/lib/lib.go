// 라이브러리 접근 제어 1
package lib

import "fmt"

func init() {
	fmt.Println("lib Package > init start!")
}

// 다음과 같이 외부에서 함수를 접근하려면 반드시 대문자
func CheckNum(c int32) bool {
	return c > 10
}
