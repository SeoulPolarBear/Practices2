//자료형 : 맵 3

package main

import "fmt"

func main() {
	//맵(Map)
	//맴 값 변경 및 삭제

	//예제1
	map1 := map[string]string{
		"daum":   "https://daum.net",
		"naver":  "https://naver.com",
		"google": "https://google.com",
		"home1":  "https://test1.com",
	}

	fmt.Println("ex1 : ", map1)

	map1["home2"] = "https://test2.com" // 추가

	fmt.Println("ex1 : ", map1)

	map1["home2"] = "https://test2-2.com" // 수정

	fmt.Println("ex1 : ", map1)

	delete(map1, "home2") // 삭제

	fmt.Println("ex1 : ", map1)

	fmt.Println()

}
