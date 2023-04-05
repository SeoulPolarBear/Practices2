//함수 기초 2

package main

import (
	"fmt"
)

func sum(i int, f func(int, int)) {
	f(i, 10)
}

func add(a int, b int) {
	fmt.Println("ex1 : ", a+b)
}

func multi_value(i int) {
	i = i * 10
}

func multi_reference(i *int) {
	*i *= 10
}

// func : 함수
func main() {
	//함수(콜백) 전달, 참조 전달(call by reference), 값 전달(call by value)
	//예제1
	sum(100, add) // 함수 전달 C++에서 <T>와 같은 역할을 한다.

	//예제2
	//call by value
	a := 100
	multi_value(a)
	fmt.Print("ex2 : ", a)

	//예제3
	//call by reference
	b := 100
	multi_reference(&b)
	fmt.Print("ex3 : ", b)

}