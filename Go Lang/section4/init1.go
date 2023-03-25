//go 초기화 함수 1

package main

import (
	"fmt"
)

func init() {
	fmt.Println("Init Method Start")
}
func main() {
	//init : 패키지 로드시에 가장 먼저 호출 즉, main 함수보다 먼저 시작된다.
	// 가장 먼저 초기화 되는 작업 작성시 유용하다.
	fmt.Println("Main Method Start!")
}
