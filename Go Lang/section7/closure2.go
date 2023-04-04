//함수 Closure 2

package main

import "fmt"

func main() {
	//예제1
	//가비지 컬렉터로 수거를 한다.
	cnt := increaseCnt()
	fmt.Println("ex1 : ", cnt()) //1
	fmt.Println("ex1 : ", cnt()) //2
	fmt.Println("ex1 : ", cnt()) //3
	fmt.Println("ex1 : ", cnt()) //4
	fmt.Println("ex1 : ", cnt()) //5
}

func increaseCnt() func() int { //반환형이 int인 함수를 리턴
	n := 0 //지역변수(캡처됨) 즉, 함수 외부에서 n을 기억하고 있어서 결과가 누적되서 나온다.
	return func() int {
		n += 1
		return n
	}
}
