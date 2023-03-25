// 패키지 1
package main

import (
	"fmt"
	"os"
)

//선언 방법
// import "fmt"
// import "os"

//선언 방법 2

func main() {
	// 패키지 : 코드 구조화(모듈) 및 재사용
	// 음집도, 결합도
	// Go : 패키지 단위의 독립적이고 작은 단위로 개발
	// -> 작은 패키지를 결합해서 프로그램을 작성 할 것을 구너고
	// 패키지 이름 = 디렉토리 이름
	// 같은 패키지 내 -> 소스파일들은 디렉토리명을 패키지 명으로 사용한다.
	// 네이밍 규칙 : 소문자 private, 대문자 : public
	// 즉, 폴더 내에서만 사용하려면 소문자로, 다른 폴더에서 사용하려면 첫글자를 대문자로 하면 된다.
	// Go : main 패키지는 특별하게 인식 -> 컴파일러 공유 라이브러리 x, 프로그램의 시작점 start point
	// 즉, 다른 파일들은 부모 dir를 package로 가져야 하지만 main 파일은 제외

	var name string

	fmt.Println("이름은? : ")
	fmt.Scanf("%s", &name)
	fmt.Fprintf(os.Stdout, "Hi! %s\n", name)
}
