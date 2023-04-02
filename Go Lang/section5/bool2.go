// 데이터 타입 : Bool 2
package main

import "fmt"

func main() {

	//예제 1
	fmt.Println("ex1 : ", true && true)   // true
	fmt.Println("ex1 : ", true && false)  // false
	fmt.Println("ex1 : ", false && false) // false
	fmt.Println("ex1 : ", true || true)   // true
	fmt.Println("ex1 : ", true || false)  // true
	fmt.Println("ex1 : ", false || false) // false
	fmt.Println("ex1 : ", !true)          // false
	fmt.Println("ex1 : ", !false)         // true

	//예제 2
	num1 := 15
	num2 := 37

	fmt.Println("ex2 : ", num1 < num2)  // true
	fmt.Println("ex2 : ", num1 > num2)  // false
	fmt.Println("ex2 : ", num1 <= num2) // true
	fmt.Println("ex2 : ", num1 >= num2) // false
	fmt.Println("ex2 : ", num1 == num2) // false
	fmt.Println("ex2 : ", num1 != num2) // true

}
