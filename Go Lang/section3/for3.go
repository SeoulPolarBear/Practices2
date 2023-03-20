//for 문 3

package main

import "fmt"

func main() {
	//예제1
Loop1:
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if i == 2 && j == 4 {
				break Loop1
				// 그냥 break를 샤용하면 j가 있는 for만 빠져나기지만
				// break Loop1을 사용하면 Loop1을 빠져나가서 이중 for문을 빠져나가게 된다.
			}
			fmt.Println("ex1 :", i, j)
		}
	}

	//예제2
	for i := 0; i < 10; i++ {
		if i%2 == 0 {
			continue
		}
		fmt.Println("ex2 :", i)
	}

	//예제3 무한루프 사용
Loop2:
	// 에러 발생(Loop 레이블 밑에 관련이 없는 소스코드가 있을 시 에러)
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if i == 1 && j == 2 {
				continue Loop2
				// continue Loop2을 사용하면
				//  (0,0) (0,1) (0,2)
				//  (1,0) (1,1) (1,2)
				//  (2,0) (2,1) (2,2)
				//여기서 (1,2)만 제외하고 출력되게 된다.
			}
			fmt.Println("ex1 :", i, j)
		}
	}
}
