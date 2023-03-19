// 변수3
package main

import "fmt"

func main() {
	// 짧은 선언
	// 함수 안에서만 사용(전역 사용 불가), 선언 후 겂 할당 사 예외 발생
	// 주로 제한된 범위의 함수내에서 사용 할 경우 코드 가독성을 높일 수 있다.
	shortVar1 := 3
	shortVar2 := "Test"
	shortVar3 := false

	//shortVar1 := 10 // 이러면 에러 발생
	//shortVar3 := true // 예외 발생

	fmt.Println("shortVar1 : ", shortVar1, "shortVar2 : ", shortVar2, "shortVar3 : ", shortVar3)

	//주로 if에서 많이 사용된다
	// 여기서는 i를 일회성으로만 사용하기 때문에 이렇게 많이 사용된다.
	if i := 15; i < 11 {
		fmt.Println("Short Variable Test Success!")
	}
}
