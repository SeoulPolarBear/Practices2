//데이터 타임 : Numeric 연산1

package main

import (
	"fmt"
	"math"
)

func main() {
	//숫자 연산(산술, 비교)
	//타입이 같아야 가능
	//다른 타입끼리는 반드시 형 변환 후 연산
	//형 변환 없을 경우 예외(에러) 발생
	// +, -, *, %, / , <<, >>, & , ^

	//예제1
	var n1 uint8 = math.MaxUint8
	var n2 uint16 = math.MaxUint16
	var n3 uint32 = math.MaxUint32
	var n4 uint64 = math.MaxUint64

	fmt.Println("ex1 : ", n1) //255
	fmt.Println("ex1 : ", n2) //65535
	fmt.Println("ex1 : ", n3) //4294967295
	fmt.Println("ex1 : ", n4) //18446744073709551615
	fmt.Println()
	fmt.Println("ex1 : ", math.MaxInt8)  //255
	fmt.Println("ex1 : ", math.MaxInt16) //65535
	fmt.Println("ex1 : ", math.MaxInt32) //4294967295
	fmt.Println("ex1 : ", math.MaxInt64) //18446744073709551615
	fmt.Println()
	fmt.Println("ex1 : ", math.MaxFloat32) //3.4028234663852886e+38
	fmt.Println("ex1 : ", math.MaxFloat64) //1.7976931348623157e+308

	n5 := 100000       // int
	n6 := int16(10000) //int
	// n7 := uint8(300) // 에러 uint8은 255까지 밖에 표현이 불가하다.
	n7 := uint8(100)

	// fmt.Println("ex2 : ", n5 + n6) //에러 이유 : 형이 int, int16으로 다르므로
	fmt.Println("ex2 : ", n5+int(n6))
	fmt.Println("ex2 : ", n6+int16(n7))
	fmt.Println("ex2 : ", n6 > int16(n7))      // 비교 연산자도 마찬가지로 타입이 맞아야 한다.
	fmt.Println("ex2 : ", n6-int16(n7) > 9900) // 비교 연산자도 마찬가지로 타입이 맞아야 한다.

}
