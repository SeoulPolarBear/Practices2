//데이터 타입 : 문자열 연산 2

package main

import (
	"fmt"
)

func main() {
	//문자열 연산
	//추출, 비교 , 조합(결합)

	//예제2(비교)
	str1 := "Golang"
	str2 := "World"

	fmt.Println("ex2 : ", str1 == str2)
	fmt.Println("ex2 : ", str1 != str2)
	fmt.Println("ex2 : ", str1 > str2)
	fmt.Println("ex2 : ", str1 < str2)
	/*
		// Go 문자열 -> 아스키 코드에 대한 사전식 비교
		//abc와 ABC를 봤을 때 ABC가 더 크다 왜냐하면 a보다 A가 아스키 값이 더 커서
			ex2 :  false
			ex2 :  true
			ex2 :  false
			ex2 :  true
	*/

}
