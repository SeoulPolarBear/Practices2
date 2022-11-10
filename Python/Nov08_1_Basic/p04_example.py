# -*- coding:utf-8 -*-
import random

i = random.randint(1, 10) # 1~ 10
print(i)

#로또번호 뽑기 (6개만) (1~45) -> 중복없이 -> 출력
lotto = set()
while len(lotto) != 6:
    num1 = random.randint(1,45)
    lotto.add(num1)

for i in lotto:
    print(i, end = " ")
