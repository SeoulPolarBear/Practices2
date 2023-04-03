//자료형 : 슬라이스 심화 1

package main

import "fmt"

func main() {

	//슬라이스 추가 및 병합
	//예제 1
	s1 := []int{1, 2, 3, 4, 5} // 길이 : 5 , 메모리: 10 가정 했을 떄
	// s1 = append(s1, 6, 7, 8, 9, 10, 11)
	// 길이 : 5 -> 7, 메모리: 10 temp 20 용량 관리가 중요하다.

	s2 := []int{8, 9, 10, 11, 12}
	s3 := []int{13, 14, 15, 16, 17}

	s1 = append(s1, 6, 7)
	s2 = append(s1, s2...)      // 슬라이스를 삽입 할 경우 ... 사용
	s3 = append(s2, s3[0:3]...) // 추출 후 병합

	fmt.Println("ex1 : ", s1) //[1 2 3 4 5 6 7]
	fmt.Println("ex2 : ", s2) //[1 2 3 4 5 6 7 8 9 10 11 12]
	fmt.Println("ex3 : ", s3) //[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
	fmt.Println()

	//예제2
	s4 := make([]int, 0, 5)
	for i := 0; i < 15; i++ {
		s4 = append(s4, i)
		// 길이 및 용량 자동화
		fmt.Printf("ex2 -> len : %d, cap: %d, value: %v\n", len(s4), cap(s4), s4)
	}
	/* cap이 2배씩 늘어나는 것을 알 수 있다.
	ex2 -> len : 1, cap: 5, value: [0]
	ex2 -> len : 2, cap: 5, value: [0 1]
	ex2 -> len : 3, cap: 5, value: [0 1 2]
	ex2 -> len : 4, cap: 5, value: [0 1 2 3]
	ex2 -> len : 5, cap: 5, value: [0 1 2 3 4]
	ex2 -> len : 6, cap: 10, value: [0 1 2 3 4 5]
	ex2 -> len : 7, cap: 10, value: [0 1 2 3 4 5 6]
	ex2 -> len : 8, cap: 10, value: [0 1 2 3 4 5 6 7]
	ex2 -> len : 9, cap: 10, value: [0 1 2 3 4 5 6 7 8]
	ex2 -> len : 10, cap: 10, value: [0 1 2 3 4 5 6 7 8 9]
	ex2 -> len : 11, cap: 20, value: [0 1 2 3 4 5 6 7 8 9 10]
	ex2 -> len : 12, cap: 20, value: [0 1 2 3 4 5 6 7 8 9 10 11]
	ex2 -> len : 13, cap: 20, value: [0 1 2 3 4 5 6 7 8 9 10 11 12]
	ex2 -> len : 14, cap: 20, value: [0 1 2 3 4 5 6 7 8 9 10 11 12 13]
	ex2 -> len : 15, cap: 20, value: [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
	*/
}
