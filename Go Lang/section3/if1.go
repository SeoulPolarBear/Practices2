//If문1

package main

import "fmt"

func main() {
	//제어문(조건문)
	// IF 문 : 반드시 Boolean 검사 -> 1, 0 (사용불가 : 자동 형 변환 불가)
	// 소괄호 사용 X

	var a int = 20
	b := 20

	//예제1
	if a >= 15 {
		fmt.Println("15이상")
	}

	//예제2
	if b >= 25 {
		fmt.Println("25이상")
	}

	//에러 발생1
	// if b >= 25 //compile시 ;를 go언어 에서 자동으로 붙히기 때문
	// {
	// fmt.Println("25이상")
	// }

	//에러 발생2
	// if b >= 25 //{반드시 사용해야 한다.}
	// fmt.Println("25이상")

	//에러 발생2
	// if c := 1; c //True가 아니므로 오류 발생
	// {
	// fmt.Println("25이상")
	// }

	//예제3
	if c := 40; c >= 35 {
		fmt.Println("35이상")
	}
	// c += 20 // 오류 발생 짧은 선언에서만 사용되서

}
