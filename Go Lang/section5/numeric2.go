//데이터 타임 : Numeric 2

package main

import "fmt"

func main() {
	//데이터 타입 : 숫자형
	//정수형 문자 출력
	//예제1
	//아스키(영문)

	var char1 byte = 72
	var char2 byte = 0110
	var char3 byte = 0x48

	//예제2
	//유니코드(한글)
	var char4 rune = 50556
	var char5 rune = 0142574 //44032(8진수)
	var char6 rune = 0xC57C  // 44032(16진수)

	// %c, %d, %o, %x
	fmt.Printf("%c %c %c \n ", char1, char2, char3) // H H H
	fmt.Printf("%d %d %d \n ", char1, char2, char3) // 72 72 72
	fmt.Printf("%d %o %x \n ", char1, char2, char3) // 72 110 48

	fmt.Printf("%c %c %c \n ", char4, char5, char6) // 야 야 야
	fmt.Printf("%d %d %d \n ", char4, char5, char6) // 50556 50556 50556
	fmt.Printf("%d %o %x \n ", char4, char5, char6) // 50556 142574 c57c
}
