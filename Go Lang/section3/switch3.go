// switch문 3
package main

import "fmt"

func main() {

	//예제1 // case도 && 같은 논리 연산자도 사용할 수 있다.
	a := 30 / 15
	switch a {
	case 2, 4, 6: // i가 2, 4, 6인 경우
		fmt.Println("a -> ", a, "는 짝수")
	case 1, 3, 5: // i가 1, 3, 5인 경우
		fmt.Println("a -> ", a, "는 홀수")
	}

	//예제2
	//fallthrough는 조건에 맞는 case문 아래의 코드도 실행을 시키고 싶을 때 사용된다.
	// 따라서 go, python, ruby, c가 전부 출력된다.
	switch e := "go"; e {
	case "java":
		fmt.Println("Java!")
		fallthrough
	case "go":
		fmt.Println("go!")
		fallthrough
	case "python":
		fmt.Println("python!")
		fallthrough
	case "ruby":
		fmt.Println("ruby!")
		fallthrough
	case "c":
		fmt.Println("c!")
	}

}
