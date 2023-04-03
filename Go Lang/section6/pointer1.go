//자료형 : 포인터 1

package main

import "fmt"

func main() {
	//포인터
	//Go : 포인터 지원(c)
	//변수의 지역성, 연속된 메모리 참조 ..., 힙메모리에 저장되므로
	//파이썬(인터프리터), 자바(JRE) -> 컴파일러, 인터프리터
	//포인터지원 X (파이썬, C#, Java 등)
	//주소의 값은 직접 변경 불가능(잘못된 코딩으로 인한 버그 방지)
	//*(에스터리스크) 로 사용
	//nil 로 초기화 (nil == 0)

	//예제1
	var a *int            // 방법1
	var b *int = new(int) // 방법2

	fmt.Println(a) //<nil> //&로만 할당 가능
	fmt.Println(b) //0xc000016098
	//다음과 같이 new로 메모리를 할당하면 다음과 같이 주소를 할당해준다.

	i := 7
	fmt.Println("ex1 : ", i, &i)

	a = &i //& 주소값 전달
	b = &i

	fmt.Println("ex1 : ", a, &i) // i의 번지수
	fmt.Println("ex1 : ", &a)    // i의 번지수를 저장하고 있는 a의 번지수
	fmt.Println("ex1 : ", *a)    // 역참조 a가 가르키고 있는 번지의 실제 값
	/*
		ex1 :  0xc00009e078 0xc00009e078
		ex1 :  0xc0000c0018
		ex1 :  7
	*/
	fmt.Println()

	fmt.Println("ex1 : ", b)  // i의 번지수
	fmt.Println("ex1 : ", *b) // 역참조 a가 가르키고 있는 번지의 실제 값
	fmt.Println("ex1 : ", &b) // i의 번지수를 저장하고 있는 a의 번지수
	/*
		ex1 :  0xc00009e078
		ex1 :  7
		ex1 :  0xc0000c0020
	*/

	var c = &i
	d := &i

	*d = 10

	fmt.Println("ex1 : ", *a)
	fmt.Println("ex1 : ", *b)
	fmt.Println("ex1 : ", *c)
	fmt.Println("ex1 : ", *d)
	/* 역참조를 통해서 전부 바뀌는 것을 알 수 있다.
	ex1 :  10
	ex1 :  10
	ex1 :  10
	ex1 :  10
	*/
}
