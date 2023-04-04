//함수 기초 1

package main

import (
	"fmt"
	"strconv" // 숫자를 문자열로 바꿀 때 사용한다.
)

// 함수 선언 위치는 어느 곳이든 가능
// 예제1
func helloGolang() {
	fmt.Println("ex1 : Hello Golang!!")
}

// 예제2
func say_one(m string) {
	fmt.Println("ex2 : ", m)
}

// 예제3
func sum(x int, y int) int {
	return x + y
}

// func : 함수
func main() {
	//함수
	//선언 : func 키워드로 선언
	//func 함수명(매개변수) (반환타입 or 반환 값 변수명) : 반환 값 존재
	//func 함수명() (반환 타입 or 반환 값 변수명) : 매개변수 없음, 반환 값 존재
	//func 함수명() : 매개변수 없음, 반환 값 없음
	//타 언어와 달리 반환 값(return value) 다수 가능

	//예제1
	helloGolang()

	//예제2
	say_one("Hello World!")

	//예제3
	result := sum(5, 5)
	fmt.Println("ex3 : ", result)
	fmt.Println("ex3 : ", strconv.Itoa(sum(5, 5)))
}
