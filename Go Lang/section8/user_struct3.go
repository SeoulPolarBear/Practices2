//상용자 정의 타입 3

package main

import "fmt"

// 함수를 제정의 할 수 있다.
type totCost func(int, int) int

func describe(cnt int, price int, fn totCost) {
	fmt.Printf("cnt : %d, price: %d, orderPrice : %d", cnt, price, fn(cnt, price))
}

func main() {
	//함수 사용자 정의 타입
	var orderPrice totCost
	orderPrice = func(cnt int, price int) int {
		return (cnt * price) + 100000
	}
	//예제1
	describe(3, 5000, orderPrice)

}
