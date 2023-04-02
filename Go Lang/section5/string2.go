//데이터 타입 : 문자열 2

package main

import (
	"fmt"
)

func main() {
	//문자열
	//문자열 : UTF-8 인코딩(유니코드 문자 집합) -> 바이트 수 주의!

	//예제1
	var str1 string = "Golang"
	var str2 string = "World"
	var str3 string = "고프로그래밍"

	fmt.Println("ex1 : ", str1[0], str1[1], str1[2], str1[3], str1[4], str1[5])
	fmt.Println("ex1 : ", str2[0], str2[1], str2[2], str2[3], str2[4])
	fmt.Println("ex1 : ", str3[0], str3[1], str3[2], str3[3], str3[4], str3[5])
	/*	아스키코드 결과를 보여준다.
		ex1 :  71 111 108 97 110 103
		ex1 :  87 111 114 108 100
		ex1 :  234 179 160 237 148 132
	*/

	fmt.Printf("ex2 :%c %c %c %c %c %c\n ", str1[0], str1[1], str1[2], str1[3], str1[4], str1[5])
	fmt.Printf("ex2 :%c %c %c %c %c\n ", str2[0], str2[1], str2[2], str2[3], str2[4])
	fmt.Printf("ex2 :%c %c %c %c %c %c\n ", str3[0], str3[1], str3[2], str3[3], str3[4], str3[5])
	/*
		Println은 문자열로 사용되는데 이 때는 한글이 깨지지 않는다.
		반면 Printf는 문자를 사용하므로 한글이 깨지게 된다. 이 떄는 rune을 사용해야 한다.
			ex2 :G o l a n g
			ex2 :W o r l d
			ex2 :ê ³   í
	*/

	constr := []rune(str3)
	fmt.Printf("ex2 :%c %c %c %c %c %c\n ", constr[0], constr[1], constr[2], constr[3], constr[4], constr[5])
	/*
		다음과 같이 한글이 깨지지 않고 출력되게 하기 위해서는
		다음과 같이 rune을 사용하면 된다.
		결과 : 고 프 로 그 래 밍
	*/

	//예제3 // index, 문자
	for i, char := range str1 {
		fmt.Printf("ex3 : %c(%d)\t", char, i)
	}
	/*
		ex3 : G(0)     ex3 : o(1)      ex3 : l(2)      ex3 : a(3)      ex3 : n(4)      ex3 : g(5)
	*/
	fmt.Println()
	for i, char := range str2 {
		fmt.Printf("ex4 : %c(%d)\t", char, i)
	}
	/*
		ex4 : W(0)      ex4 : o(1)      ex4 : r(2)      ex4 : l(3)      ex4 : d(4)
	*/

}
