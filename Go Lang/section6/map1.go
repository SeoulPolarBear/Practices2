//자료형 : 맵 1

package main

import "fmt"

func main() {
	//맵(Map)
	//맵 : 해시테이블, 딕셔너리(파이썬), key-value로 자료 저장
	//레퍼런스 타입(참조 값 전달)
	//비교 연산자 사용 불가능(참조 타입이므로)
	//특징 : 참조타입(key)로 key 사용 불가능, 값(value)으로 모든 타입 사용가능
	//make 함수 및 축약(리터럴)로 초기화 가능
	//순서 없음

	//예제1 리터럴로 선언
	var map1 map[string]int = make(map[string]int) // 정석
	var map2 = make(map[string]int) // 자료형 생략
	map3 := make(map[string]int) // 리터럴 형태(쩗은 선언)

	fmt.Println("ex1 : ", map1) // map[]
	fmt.Println("ex1 : ", map2) // map[]
	fmt.Println("ex1 : ", map3) // map[]

	//예제2
	map4 := map[string]int{} // Json 형태 a = {}
	map4["apple"] = 25
	map4["banana"] = 40
	map4["orange"] = 33

	map5 := map[string]int{
		"appel": 15,
		"banana" : 40,
		"orange" : 23,
	}

	map6 := make(map[string]int,10)
	map["apple"] = 25
	map["banana"] = 40
	map["orange"] = 33

	fmt.Println("ex1 : ", map4) 
	fmt.Println("ex1 : ", map5) 
	fmt.Println("ex1 : ", map6) 
	fmt.Println("ex1 : ", map4["apple"]) 
	fmt.Println("ex1 : ", map5["banana"]) 
	fmt.Println("ex1 : ", map6["orange"])
}
