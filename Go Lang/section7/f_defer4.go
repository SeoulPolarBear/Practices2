//함수 Defer 3

package main

import (
	"fmt"
)

func start(t string) string {
	fmt.Println("start : ", t)
	return t
}

func end(t string) {
	fmt.Println("end : ", t)
}

func a() {
	defer end(start("b"))
	fmt.Println("in a")
}

func main() {

	//예제1
	a()
	/*
		즉, defer(지연) 함수는 defer가 있는 함수만 나중으로 미루고
		그 안에 만약 함수를 사용하고 있으면 실행 시킨다.
		start :  b
		in a
		end :  b
	*/
}
