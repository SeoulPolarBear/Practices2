//데이터 타임 : Numeric 3

package main

import "fmt"

func main() {
	//실수(부동소수점)
	//float32(7자리), float64(15 자리)

	//예제1
	var num1 float32 = 0.14
	var num2 float32 = .75647
	var num3 float32 = 442.0378373
	var num4 float32 = 10.0

	//지수 표기법
	var num5 float32 = 14e6
	var num6 float64 = .156875e+3
	var num7 float64 = 5.32521e-10

	fmt.Println("ex1 : ", num1) //0.14
	fmt.Println("ex1 : ", num2) //0.75647

	//442.0378373 5의 자리에서 반올림 최종 7개의 숫자만 보여준다.
	fmt.Println("ex1 : ", num3)

	fmt.Println("ex1 : ", num4)              //10
	fmt.Println("ex1 : ", num4-0.1)          //9.9
	fmt.Println("ex1 : ", float32(num4-0.1)) //9.9

	// 부동 소수점 오차 금융권에서 조심해야 한다. 따라서 처음부터 64 같은 것을 넉넉히 줘야 한다.
	fmt.Println("ex1 : ", float64(num4-0.1)) //9.899999618530273 : 15개의 자리 표현

	fmt.Println("ex1 : ", num5) //1.4e+07
	fmt.Println("ex1 : ", num6) //156.875
	fmt.Println("ex1 : ", num7) //5.32521e-10
}
