// 상수1
package main

import "fmt"

func main() {
	//상수
	//const 사용 초기화, 한 번 선언 후 값 변경 금지, 고정된 값 관리용
	const a string = "Test1"
	const b = "Test2"
	const c int32 = 10 * 10
	//const d = getHeight() // 오류 발생 이유 : return 값 자체가 불변이 아니므로
	const e = 35.6
	const f = false

	/*
		에러 발생
		const g string
		g = "Test3"
		즉, const는 선언 시 바로 초기화 시켜야 한다.
	*/

	fmt.Println("a : ", a)
	fmt.Println("b : ", b)
	fmt.Println("c : ", c)
	fmt.Println("e : ", e)
	fmt.Println("f : ", f)

}
