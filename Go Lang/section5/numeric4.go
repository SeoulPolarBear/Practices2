//데이터 타임 : Numeric 4

package main

import "fmt"

func main() {
	//데이터 타입 : 숫자형
	//복소수 형 (complex number)
	//complex64(32bit 실수 + 허수)
	//complex128(64bit 실수 + 허수)

	//예제1
	var num1 complex64 = 5 + 7i
	num2 := 8 + 1i
	num3 := complex(3, 2) // complex128 이유 : 내 pc가 64bit여서 실수, 허수 각각해서 128
	var num4 complex128 = 9 + 3i
	num5 := complex64(2 + 3i)

	fmt.Println("ex1 : ", num1) //(5+7i)
	fmt.Println("ex1 : ", num2) //(8+1i)
	fmt.Println("ex1 : ", num3) //(3+2i)
	fmt.Println("ex1 : ", num4) //(9+3i)
	fmt.Println("ex1 : ", num5) //(2+3i)

	//예제2
	//real() : 실수부 출력
	//imag() : 허수부 출력
	fmt.Println("ex2 : ", num1, real(num1), imag(num1)) //(5+7i) 5 7
	fmt.Println("ex2 : ", num2, real(num2), imag(num2)) //(8+1i) 8 1
	fmt.Println("ex2 : ", num3, real(num3), imag(num3)) //(3+2i) 3 2
	fmt.Println("ex2 : ", num4, real(num4), imag(num4)) //(9+3i) 9 3
	fmt.Println("ex2 : ", num5, real(num5), imag(num5)) //(2+3i) 2 3
}
