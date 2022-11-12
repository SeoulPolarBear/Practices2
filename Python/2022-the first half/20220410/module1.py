#모듈을 사용하는 이유
# 프로그램 기능별로 파일을 나누어서 유지보수 등 관리를 편하게 하는데 있다.

# 모듈의 개념 : 한개의 완성된 프로그램 파일

# 파이썬 기본 모듈 사용방법
# import 모듈 이름
# 모듈이름.변수
# 모듈이름.함수()

# 별칭을 이용한 명시적 모듈 임포팅

import math # 모듈 네임스페이스 임포팅 ex) math라는 모듈의 모든 함수를 쓰고 싶을 때 이렇게 사용한다.
#from math import * 와 같은 상황이다. 하지만 차이점이 있다. 
#from math import * 인 경우는 load를 하므로 math의 함수들을 가져와서 복붙했다고 생각하면된다. 그럼 오버라이딩 될 수 있다.
#반면 import math의 경우는 math에 접근하기 때문에 그나마 overriding에 대한 대비는 할 수 있다. (이건 math에 직접 접근하므로)
#단점으로 낭비가 될 수 있다.

print(math.pi)
print(math.ceil(5.7))

import math as ma # 모듈 네임스페이스 임포팅

# 또는 

from math import pi, ceil # 모듈에서 사용할 수 있는 특정 함수를 지정해서 임포트
                            #명시적 모듈 컨텐츠 임포팅(선언한 값만 가져오겠다.), 좋은 선언 방식이 아니다.
                            
print(pi)
print(ceil(5.7))

from math import * #묵시적 모듈 컨텐츠 임포팅(모두 가져오겠다.)
#치명적인 단점은 일단 math를 가져왔는데 만약 같은 이름의 함수를 내가 만들면 오버라이딩이 될 수 있다.

print(sum(range(5),-1))
# 결과 > 9

#from numpy import *
import numpy
print(numpy.sum(range(5),-1))
#결과 > 10


from math import pi,ceil as c # ceil as c는 c 문자로 단축
print(pi)
print(c(2.7))