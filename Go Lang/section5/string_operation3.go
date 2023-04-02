//데이터 타입 : 문자열 연산 3

package main

import (
	"fmt"
	"strings"
)

func main() {
	//문자열 연산
	//추출, 비교 , 조합(결합)

	//예제1(결합 : 일반연산)
	str1 := "The Go programming language is an open source project to make programmers more productive." +
		"Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked" +
		"machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage" +
		"collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language."

	str2 := "Introduces the basics of creating and using multi-module workspaces in Go. Multi-module workspaces are useful for making changes across multiple modules."

	fmt.Println("ex1 : ", str1+str2)

	//golang benchmark 를 확인해서 Join이 연산보다 좋다는 것을 확인해보자
	//예제2 (결합 : Join)
	//1. 배열에 string을 넣는다.
	//2. Join을 이용해서 합친다. python이랑 똑같다.
	strSet := []string{} // 슬라이스 선언
	strSet = append(strSet, str1)
	strSet = append(strSet, str2)

	fmt.Println("ex2 : ", strings.Join(strSet, "----------"))
}
