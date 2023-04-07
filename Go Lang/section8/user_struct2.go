//상용자 정의 타입 2

package main

import "fmt"

type cnt int

func main() {
	//기본 자료형

	//예제1
	a := cnt(5)
	fmt.Println("ex1 : ", a)

	//예제2

	var b cnt = 15
	fmt.Println("ex1 : ", b)

	//예제 3
	// 에러 발생 : int로 사용은 되지만 cnt와 int가 엄연히 다르다고 인식한다.
	// 사용자 정의 타입 <-> 기본 타입 : 매개 변수 전달 시에 변환해야 사용가능(cnt)
	// testConverT(b)
	testConverT(int(b))
	testConverD(b)
}

func testConverT(i int) {
	fmt.Println("ex3 : (Default Type)", i)
}

func testConverD(i cnt) {
	fmt.Println("ex3 : (Custom Type)", i)
}
