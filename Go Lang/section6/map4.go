//자료형 : 맵 4

package main

import "fmt"

func main() {
	//맵(Map)
	//맴 조회할 경우 주의할 점

	//예제1
	map1 := map[string]int{ // int : 0, string: "", float: 0.0
		"appel":  15,
		"banana": 115,
		"orange": 1115,
		"lemon":  0,
	}

	value1 := map1["banana"]
	value2 := map1["kiwi"]
	value3, ok := map1["kiwi"]

	fmt.Println("ex1 : ", value1)
	fmt.Println("ex1 : ", value2)
	// error가 아닌 초기값 0을 출력 하지만 key가 존재하는지 확인이 불가능
	fmt.Println("ex1 : ", value3, ok)
	// 위의 문제를 해결하기 위해서 return값을 2개로 ok는 존재 유무이다.

	//예제2

	if value, ok := map1["kiwi"]; ok {
		fmt.Println("ex2 : ", value)
	} else {
		fmt.Println("ex2 : kiwi is not exist!")
	}

	if value, ok := map1["banana"]; ok {
		fmt.Println("ex2 : ", value)
	} else {
		fmt.Println("ex2 : banana is not exist!")
	}

	if _, ok := map1["kiwi"]; !ok {
		fmt.Println("ex2 : banana is not exist!")
	}
}
