//자료형 : 슬라이스 2

package main

import "fmt"

func main() {

	//슬라이스(슬라이스 참조 타입 증명)

	//예제 1 (배열)
	arr1 := [3]int{1, 2, 3}
	var arr2 [3]int

	arr2 = arr1 // 값 복사에 의한 선언
	arr2[0] = 7

	fmt.Println("ex1 : ", arr1)
	fmt.Println("ex1 : ", arr2)
	fmt.Println()

	//예제 2 (슬라이스)
	slice1 := []int{1, 2, 3} //참조(메모리 주소)를 대입
	var slice2 []int
	slice2 = slice1
	slice2[0] = 7

	fmt.Println("ex2 : ", slice1)
	fmt.Println("ex2 : ", slice2)
	fmt.Println()

	//예제 3(슬라이스 예외 상황)
	slice3 := make([]int, 50, 100)
	fmt.Println("ex3", slice3[4]) // 결과 0

	fmt.Println("ex3", slice3[50]) // 결과 index out of range
	//즉, make 함수를 사용할 때 메모리 측정은 int * 슬라이스의 길이(50)으로 초기화
	fmt.Println()

	//예제4(슬라이스 순회)
	for i, v := range slice1 {
		fmt.Println("ex4 : ", i, v)
	}
	//0 7 / 1 2 / 2 3

}
