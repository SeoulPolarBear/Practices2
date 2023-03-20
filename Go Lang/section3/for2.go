//for 문 2

package main

import "fmt"

func main() {
	//예제1
	sum1 := 0
	for i := 0; i < 100; i++ {
		sum1 += i
	}
	fmt.Println("ex1 :", sum1)

	//예제2 자주 사용되는 방법
	sum2, i := 0, 0
	for i < 100 {
		sum2 += i
		i++
		//j := i++ //에러 난다 이유 : Go에서 후치연산은 반환 값이 없다.
	}
	fmt.Println("ex2 :", sum2)

	//예제3 무한루프 사용
	sum3, i := 0, 0

	for {
		if i >= 100 {
			break
		}
		sum3 += i
		i++
	}
	fmt.Println("ex2 :", sum3)

	//예제4 즉, 다양한 변수를 한번에 사용할 수 있는 것이 장점이라 할 수 있다.
	for i, j := 0, 0; i <= 10; i, j = i+1, j+10 {
		fmt.Println("ex4 : ", i, j)
	}

	//에러 발생
	// for i, j := 0, 0; i <= 10; i++, j = j+10 { //이유 : 후치연산은 반환값이 없기 때문에
	// 	fmt.Println("ex4 : ", i, j)
	// }
}
