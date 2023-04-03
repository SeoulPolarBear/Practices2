//자료형 : 슬라이스 심화 3

package main

import (
	"fmt"
)

func main() {

	//슬라이스 복사
	//copy(복사 대상 ,원본)
	//make로 공간을 할당 후 복사 해야한다.
	//복사 된 슬라이스 값 변경해도 원본에는 영향 없음

	//예제 1 복사
	slice1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	slice2 := make([]int, 5)
	slice3 := []int{}

	copy(slice2, slice1) //[1 2 3 4 5]
	// slice2는 make로 생성 할당 길이가 5이므로 5개만 카피
	copy(slice3, slice1) //[]
	// slice3 make로 생성 X 따라서 빈 슬라이스가 그대로 출력된다.

	fmt.Println("ex1 : ", slice1)
	fmt.Println("ex1 : ", slice2)
	fmt.Println("ex1 : ", slice3)

	//예제2
	a := []int{1, 2, 3, 4, 5}
	b := make([]int, 5)

	copy(b, a)

	b[0] = 7
	b[4] = 10

	fmt.Println("ex1 : ", a) //[1 2 3 4 5]
	fmt.Println("ex1 : ", b) //[7 2 3 4 10]

	fmt.Println()

	//예제3
	//값에 의한 참조일지 주소에 의한 참조인지 확인
	c := [5]int{1, 2, 3, 4, 5}
	d := c[0:3] // 주의! 부분적으로 슬라이스 추출은 참조 -> 원본 값 변경 된다.

	d[1] = 7
	// 주소에 의한 참조임을 알 수 있다.
	fmt.Println("ex1 : ", c) //[1 7 3 4 5]
	fmt.Println("ex1 : ", d) //[1 7 3]

	fmt.Println()

	//예제4
	e := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	f := e[0:5:7] //용량 지정
	// 길이는 5이고 복사시 메모리를 7로 지정해서 복사를 하라는 뜻이 된다.

	fmt.Println("ex4 : ", len(f), cap(f)) // 5 7
	fmt.Println("ex4 : ", f)              // [1 2 3 4 5]
}
