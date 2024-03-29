//자료형 : 슬라이스 1

package main

import "fmt"

func main() {
	// 길이의 개념이 없다. (가변이므로) -> 동적으로 크기가 늘어난다. 레퍼런스(참조 값) 타입
	//슬라이스 (길이 & 용량) 크기가 동적으로 할당 가능
	//배열 vs 슬라이스 차이점 중요
	//길이고정 vs 길이 가변
	//※★값 타입 vs 참조 타입★※
	//복사 전달 vs 참조 값 전달
	//전체 비교연산자 사용 가능 vs 비교 연산자 사용불가
	//대부분 슬라이스 사용한다.

	//2가지 선언 방법 1. 배열처럼 선언, 2. make 함수 : make(자료형, 길이, 용량(생략시 길이))

	//예제 1 //즉, 배열은 개수를 []에 적어줘야하는데 슬라이스는 그럴 필요가 없다.
	var slice1 []int
	slice2 := []int{}
	slice3 := []int{1, 2, 3, 4, 5}
	slice4 := [][]int{
		{1, 2, 3, 4, 5},
		{6, 7, 8, 9, 10},
	}
	//------------유의사항----------------------
	// slice2[0] = 1 // 값 수정 불가능
	//이유 : 슬라이스는 가변이므로 초기화를 확실히 하지 않으면 값을 수정할 수 없다.
	slice3[4] = 10 // 값 수정 가능
	//-----------------------------------

	// len : 슬라이스 길이, cap : 슬라이스 용량
	fmt.Printf("%-5T %d %d %v\n", slice1, len(slice1), cap(slice1), slice1)
	fmt.Printf("%-5T %d %d %v\n", slice2, len(slice2), cap(slice2), slice2)
	fmt.Printf("%-5T %d %d %v\n", slice3, len(slice3), cap(slice3), slice3)
	fmt.Printf("%-5T %d %d %v\n", slice4, len(slice4), cap(slice4), slice4)

	//예제2
	// 10개의 메모리를 할당 받고 그 중 5개의 메모리를 사용하겠다는 뜻이다.
	// 최적화를 하기에 좋은 함수이다.

	//var slice5 []int = make([]int, 5)이렇게 작성도 할 수 있다.
	var slice5 []int = make([]int, 5, 10)
	var slice6 []int = make([]int, 5)
	slice7 := make([]int, 5, 10)
	slice8 := make([]int, 5)

	slice6[2] = 7 // 삽입

	//  make로 초기화를 하면 integer는 0으로 초기화 되는 것을 알 수 있다.
	fmt.Printf("%-5T %d %d %v\n", slice5, len(slice5), cap(slice5), slice5)
	fmt.Printf("%-5T %d %d %v\n", slice6, len(slice6), cap(slice6), slice6)
	fmt.Printf("%-5T %d %d %v\n", slice7, len(slice7), cap(slice7), slice7)
	fmt.Printf("%-5T %d %d %v\n", slice8, len(slice8), cap(slice8), slice8)

	//예제 3
	var slice9 []int // nil 슬라이스(깅이와 용량 0)

	if slice9 == nil {
		fmt.Println("This is Nil Slice!")
	}

}
