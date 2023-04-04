//함수 Defer 3

package main

import (
	"fmt"
)

func stack() {
	for i := 1; i <= 10; i++ {
		defer fmt.Println("ex1 : ", i)
	}
}

func main() {

	//예제1
	stack()
	/*
		ex1 :  10
		ex1 :  9
		ex1 :  8
		ex1 :  7
		ex1 :  6
		ex1 :  5
		ex1 :  4
		ex1 :  3
		ex1 :  2
		ex1 :  1
	*/
}
