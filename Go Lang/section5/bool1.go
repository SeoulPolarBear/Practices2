// 데이터 타입 : Bool 1
package main

import "fmt"

func main() {
	// Bool(Boolean) : 참과 거짓
	// 조건부 논리 연산자랑 주로 사용 : !, || &&
	// 암묵적 형변환 X : 0, NULL -> False 변환 없음

	//예제 1
	var b1 bool = true
	var b2 bool = false
	b3 := true

	fmt.Println("ex1 : ", b1)
	fmt.Println("ex2 : ", b2)
	fmt.Println("ex3 : ", b3)

	fmt.Println("ex4 : ", b3 == b3)
	fmt.Println("ex4 : ", b1 || b3)
	fmt.Println("ex4 : ", b2 && b3)
	fmt.Println("ex4 : ", !b1)

	// 암묵적 형 변환 사용 금지
	// b4 := 1
	// if b4 {
	// 	fmt.Println("ex8 : true!")
	// }
}
