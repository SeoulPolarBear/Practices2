// 상수2
package main

import "fmt"

func main() {
	const a, b int = 10, 99
	const c, d, e = true, 0.84, "test"
	const (
		x, y int16 = 50, 90
		i, k       = "Data", 7776
	)
	fmt.Println("a : ", a)
	fmt.Println("b : ", b)
	fmt.Println("c : ", c)
	fmt.Println("d : ", d)
	fmt.Println("e : ", e)
	fmt.Println("x : ", x)
	fmt.Println("y : ", y)
	fmt.Println("i : ", i)
	fmt.Println("k : ", k)
}
