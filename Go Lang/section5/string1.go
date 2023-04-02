//데이터 타입 : 문자열 1

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	//문자열
	//큰 따옴표 "", 백스쿼드 ``
	//GoLang : 문자 char 타입 존재 하지 않음 -> rune(int32)로 문자 코드 값으로 표현
	//문자 : '' 로 작성
	//자주 사용하는 escape : \\, \', \", \a(콘솔벨), \b(백스페이스),
	//\f(쪽 바꿈), \n(줄 바꿈), \r(복귀), \t(탭),...

	//예제1
	var str1 string = "c:\\go_study\\src\\" // -> c:/go_study/src/
	str2 := `c:/go_study/src/`

	fmt.Println("ex1 : ", str1)
	fmt.Println("ex1 : ", str2)

	//예제2
	var str3 string = "Hello, world!"
	var str4 string = "안녕하세요."
	var str5 string = "\ud55c\ucae00" // 유니코드로 사용은 가능

	fmt.Println("ex2 : ", str3) // Hello, world!
	fmt.Println("ex2 : ", str4) // 안녕하세요.
	fmt.Println("ex2 : ", str5) // 한글

	//예제3
	//길이(바이트 수) 알파벳 : 1바이트 사용 / 한글은 3바이트 사용
	fmt.Println("ex3 : ", len(str3)) // 13 문자 사용 byte
	fmt.Println("ex3 : ", len(str4)) // 3 * 5 + 1 = 16 byte

	//예제4
	//길이(실제 길이)
	fmt.Println("ex4 : ", utf8.RuneCountInString(str3)) // 13
	fmt.Println("ex4 : ", utf8.RuneCountInString(str4)) // 6
	fmt.Println("ex4 : ", len([]rune(str4)))            // 6
	//len으로 실제 길이 구하는 법
}
