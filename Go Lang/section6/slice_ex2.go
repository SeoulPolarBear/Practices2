//자료형 : 슬라이스 심화 2

package main

import (
	"fmt"
	"sort"
)

func main() {

	//슬라이스 추출 및 정렬
	//slice[i:j] -> 범위 : [i,j)
	//slice[i:] -> 범위 : i에서 마지막 까지 추출
	//slice[:j] -> 처음부터 j-1까지 추출
	//slice[:] -> 처음부터 마지막까지 추출

	//예제 1 추출
	slice1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println("ex1 : ", slice1[0:3])           //[1 2 3 ]
	fmt.Println("ex1 : ", slice1[0:])            //[1 2 3 4 5 6 7 8 9 10]
	fmt.Println("ex1 : ", slice1[:3])            //[1 2 3 ]
	fmt.Println("ex1 : ", slice1[:])             //[1 2 3 4 5 6 7 8 9 10]
	fmt.Println("ex1 : ", slice1[1:len(slice1)]) //[2 3 4 5 6 7 8 9 10]

	//예제 2 정렬
	//sort 패키지 : https://golang/org/pkg/sort
	slice2 := []int{3, 7, 10, 1, 2, 6, 4, 9, 5, 8}
	slice3 := []string{"b", "a", "c", "d", "e", "f"}

	fmt.Println("ex2 : ", sort.IntsAreSorted(slice2)) //false
	// 정렬이 되었는지 확인하는 메소드
	sort.Ints(slice2) // 정렬하는 메소드
	fmt.Println("ex2 : ", slice2)

	fmt.Println()

	fmt.Println("ex3 : ", sort.StringsAreSorted(slice3)) //false
	// 정렬이 되었는지 확인하는 메소드
	sort.Strings(slice3) // 정렬하는 메소드
	fmt.Println("ex3 : ", slice3)

	fmt.Println()
}
