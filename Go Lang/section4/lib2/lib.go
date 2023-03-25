// 라이브러리 접근 제어 2
package lib2

// 다음과 같이 외부에서 함수를 접근하려면 반드시 대문자
func CheckNum1(c int32) bool {
	return c > 10
}

func CheckNum2(c int32) bool {
	return c > 1000
}
