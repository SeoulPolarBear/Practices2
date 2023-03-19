// 열거형 3
package main

import "fmt"

func main() {
	const (
		_ = iota // _는 생략할 떄 사용할 수 있다.
		A        //1
		B        //2
		C        //3
	)

	const (
		_ = iota + 0.75*2 // 즉, 이렇게 규칙을 미리 만들어놔서
		// 볼 수 있게도 활용이 가능하다.
		DEFAULT
		SILVER
		GOLD
		PLATINUM
	)
	fmt.Println("D : ", DEFAULT, "S : ", SILVER, "G : ", GOLD, "P : ", PLATINUM)
}
