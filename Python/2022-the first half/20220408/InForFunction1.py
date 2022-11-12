[val if val % 2 else -val
 for val in range(20) if val % 3]
#반드시 개행을 해줘야 한다.
# 결과
#[1, -2, -4, 5, 7, -8, -10, 11, 13, -14, -16, 17, 19]
#for val in range(20) if val % 3 for 안에 if문을 통해서 list를 만들어 준다고 생각하면 된다.

