//데이터 타임 : Numeric 1

package main

import "fmt"

func main() {
	//데이터 타입 : 숫자형
	//정수, 실수, 복소수
	//32bit, 64bit, unsigned(양수)
	//정수 : 8진수(0), 16진수(0x), 10진수

	var num1 int = 17
	var num2 int = -68
	var num3 int = 0631
	// 8진수 6*8^2 + 3*8^1 + 1*8^0

	var num4 int = 0x32fa2c75
	// 16진수 3*16^7 + 2*16^6 + 15*16^5 + 10*16^4 + 2*16^3 + 12*16^2 + 7*16^1 + 5*16^0

	fmt.Println("ex1 : ", num1)
	fmt.Println("ex1 : ", num2)
	fmt.Println("ex1 : ", num3)
	fmt.Println("ex1 : ", num4)

}
