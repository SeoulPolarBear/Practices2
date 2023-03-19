// 변수2
package main

import "fmt"

func main() {
	//여러개 선언
	//장점 : 하나의 그룹으로 보이므로 객체의 상태를 가독성 있게 볼 수 있다.
	var (
		name      string = "machine"
		height    int32
		weight    float32
		isRunning bool
	)

	height = 250
	weight = 320.56
	isRunning = true

	fmt.Println("name : ", name, "height : ", height, "weight : ", weight, "isRunning : ", isRunning)
}
