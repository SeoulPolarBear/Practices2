//자료형 : 맵 3

package main

import "fmt"

func main() {
	//맵(Map)
	//맴 조회 및 순화(Iterator)

	//예제1
	map1 := map[string]string{
		"daum":   "https://daum.net",
		"naver":  "https://naver.com",
		"google": "https://google.com",
	}

	fmt.Println("ex1 : ", map1["google"])
	fmt.Println("ex1 : ", map1["daum"])
	fmt.Println("ex1 : ", map1["naver"])

	fmt.Println()

	//예제2(순서 없으므로 랜덤)
	for k, v := range map1 {
		fmt.Println("ex2 : ", k, v)
	}

	fmt.Println()

	for _, v := range map1 {
		fmt.Println("ex2 : ", v)
	}

}
