//Go 특징 2

package main

import "fmt"

func main() {
	//코드 서식 지정
	//한 사람이 코딩 한 것 같은 일관성 유지
	//코드 스타일 유지
	//gofmt -h 파일이름: 사용법
	//gofmt -w 파일이름: 원본파일에 반영
	//VSCode가 알아서 해준다.
	//만약 확인하고 싶으면 txt에서 확인하면 된다.

	//예제1
	for i := 0; i <= 100; i++ {
		fmt.Println("ex1 :", i)
	}
}
