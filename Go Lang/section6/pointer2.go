//자료형 : 포인터 2

package main

import "fmt"

func main() {
	//포인터

	//예제1
	i := 7
	p := &i

	fmt.Println("ex1 : ", i, *p, &i, p) // 7, 7, p의 값
	//ex1 :  7 7 0xc000018098 0xc000018098

	*p++                                // i의 값이 8이 된다.
	fmt.Println("ex1 : ", i, *p, &i, p) // 8, 8, p의 값
	//ex1 :  8 8 0xc000018098 0xc000018098

	*p = 7777 //포인터 변수 역 참조 값 변경

	fmt.Println("ex1 : ", i, *p, &i, p) // 8, 8, p의 값
	//ex1 :  7777 7777 0xc000018098 0xc000018098

	i = 77
	fmt.Println("ex1 : ", i, *p, &i, p) // 8, 8, p의 값
	//ex1 :  77 77 0xc000018098 0xc000018098
}
