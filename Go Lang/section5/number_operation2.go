//데이터 타임 : Numeric 연산 2

package main

import (
	"fmt"
)

func main() {
	//예제1
	var n1 uint8 = 125
	var n2 uint8 = 90

	fmt.Println("ex1 : ", n1+n2) // 215
	fmt.Println("ex1 : ", n1-n2) // 35
	fmt.Println("ex1 : ", n1*n2) // 242
	fmt.Println("ex1 : ", n1/n2) // 1
	fmt.Println("ex1 : ", n1%n2) // 35
	fmt.Println("ex1 : ", n1<<2) // 244
	fmt.Println("ex1 : ", n1>>2) // 31
	fmt.Println("ex1 : ", ^n1)   // 01111101 -> 10000010 = 130
	fmt.Println("ex1 : ", n1&n2) // 01111101 & 01011010 -> 01011000 = 88
	fmt.Println("ex1 : ", n1|n2) // 01111101 | 01011010 -> 01111111 = 127
	fmt.Println()

	//예제2
	var n3 int = 12
	var n4 float32 = 8.2
	var n5 uint16 = 1024
	var n6 uint32 = 120000

	// fmt.Println("ex3 : ", n3 + n4) 에러
	fmt.Println("ex3 : ", float32(n3)+n4) // 20.2
	fmt.Println("ex3 : ", n3+int(n4))     // 20 이유 : 소수점 버림
	fmt.Println("ex3 : ", n5+uint16(n6))  // 55488 = 1024 + 54464
	// 이유 :uint16은 65535까지 밖에 표현을 못해서
}
