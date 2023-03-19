// 변수1
package main

import "fmt"

func main() {
	//기본 초기화
	// int : 64비트 시스템에서는 64bit, 32비트 시스템에서는 32bit이다.
	//정수타입 : 0, -> int, int8, int16, int32, int64
	//unsigned : uint, uint8, uint16, uint32, uint64
	//uintptr : uint와 크기가 동일하며 포이터를 저장할 때 사용된다.
	//단위 : bit 즉 java 인트와 같은건 int32이다.

	//---------
	//실수(소수점) : 0.0, ->
	//float32 : 32비트 배정밀도 부동소수점, 7자리 정밀도 보장
	//float64 : 64비트 배정밀도 부동소수점, 15자리 정밀도 보장
	//complex64 : float32 크기의 실수부와 허수부로 된 복소수
	//complex128 : float64 크기의 실수부와 허수부로 된 복소수

	//---------
	//기타 타입
	//byte : uint8과 크기가 동일, 바이트 단위로 저장할 떄 사용
	//rune : int32와 크기가 동일, 유니코드 문자 코드(Code point)를 저장할 때 사용

	//---------
	//문자열 : "",

	//---------
	//Boolean : True, False

	//변수명 : 숫자 첫글자x, 대소문자 구분 O, 숫자, 밑줄, 특수기호 사용 가능
	//변수 및 상수 : 함수 내외 사용 가능
	var a int
	var b string
	var c, d, e int
	var f, g, h int = 1, 2, 3
	var i float32 = 11.4
	var j string = "Hi! Golang"

	// 선언 동시 초기화
	var k = 4.74
	var l = "Hi! Seoul!"
	var m = true

	a = 4
	b = "Hello Go!"
	e = 77

	fmt.Println("a : ", a)
	fmt.Println("b : ", b)
	fmt.Println("c : ", c)
	fmt.Println("d : ", d)
	fmt.Println("e : ", e)
	fmt.Println("f : ", f)
	fmt.Println("g : ", g)
	fmt.Println("h : ", h)
	fmt.Println("i : ", i)
	fmt.Println("j : ", j)
	fmt.Println("k : ", k)
	fmt.Println("l : ", l)
	fmt.Println("m : ", m)
}
