//go 초기화 함수 2

package main

import (
	"fmt"
	"section4/lib"
)

func init() {
	fmt.Println("Init1 Method Start")
}

func init() {
	fmt.Println("Init2 Method Start")
}

func init() {
	fmt.Println("Init3 Method Start")
}

func init() {
	fmt.Println("Init4 Method Start")
}

func init() {
	fmt.Println("Init5 Method Start")
}

func main() {
	// 이렇게 되면 init 들이 순서대로 호출 된 후에 라이브러리에 있는 init을 호출 후
	// main 메서드가 실행 된다. 즉, 결국 스택에 쌓여서 사용하는 것과 같이 사용된다.
	lib.CheckNum(3)
	fmt.Println("main Source Code!")
}
