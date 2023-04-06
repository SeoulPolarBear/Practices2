//구조체 기본5

package main

import (
	"fmt"
	"reflect"
)

// 내부 참조를 위해서 앞에 대문자 사용
type Car struct {
	name    string "차량명"
	color   string "색상"
	company string "제조사"
}

func main() {
	//필드 태그 사용

	//예제1
	//reflect : 위 필드의 "색상", "제조사" 등과 같은 필드의 태그를 사용할 때 쓴다.
	tag := reflect.TypeOf(Car{})

	//NumField : struct에 필드가 몇개 인지 return 해주는 함수
	for i := 0; i < tag.NumField(); i++ {
		fmt.Println("ex1 : ", tag.Field(i).Tag, tag.Field(i).Name, tag.Field(i).Type)
	}
	/*
		ex1 :  차량명 name string
		ex1 :  색상 color string
		ex1 :  제조사 company string
	*/

}
