//구조체 기본 2

package main

import "fmt"

type Account struct {
	number   string
	balance  float64 // 잔액
	interest float64 // 이자
}

// Account를 pointer로 값을 넘겼을 때 자동으로 리시버가 매칭을 해준다.
// 대신 함수일 때는 불가능
// 리시버 함수
func (a Account) Calculate() float64 {
	return a.balance + (a.balance * a.interest)
}

func main() {
	//다양한 선언 방법
	//&struct, struct : &struct 포인터를 받아오기
	//역참조를 또 하기 때문에 속도는 조금 느리다.

	//★★★★★대신 인터페이스 메소드를 선언마 해둔 후 ->
	//오버라이딩 해서 메소드에 포인터 리시버를
	//사용할 경우 반드시  &struct로 넘겨야 한다.★★★★★★
	// structType does not implement MyInterface (DisplayA method has pointer receiver)
	//선언 방법 1
	var kim *Account = new(Account)
	kim.number = "245-901"
	kim.balance = 10000000
	kim.interest = 0.015

	//선언 방법2
	hong := &Account{number: "245-902", balance: 15000000, interest: 0.04}

	//선언 방법3
	lee := new(Account)
	lee.number = "245-903"
	lee.balance = 13000000
	lee.interest = 0.025

	fmt.Println("ex1 : ", kim)
	fmt.Println("ex1 : ", hong)
	fmt.Println("ex1 : ", lee)
	fmt.Println()

	//#을 이용하면 포인터 형이라는 것과 포인터 구조체의 값을 전부 보여준다.
	fmt.Printf("ex2 : %#v\n", kim)
	fmt.Printf("ex2 : %#v\n", hong)
	fmt.Printf("ex2 : %#v\n", lee)

	/*
		ex2 : &main.Account{number:"245-901", balance:1e+07, interest:0.015}
		ex2 : &main.Account{number:"245-902", balance:1.5e+07, interest:0.04}
		ex2 : &main.Account{number:"245-903", balance:1.3e+07, interest:0.025}
	*/

	fmt.Println()

	//예제2
	fmt.Println("ex3 : ", int(kim.Calculate()))
	fmt.Println("ex3 : ", int(hong.Calculate()))
	fmt.Println("ex3 : ", int(lee.Calculate()))
}
