
import area # area.py module 가져오기 

# area.py에서 특정 function만 가져 온다면 
# from area import circle , sqare 
# 
# fucntion을 가져오는 경우는 
# print(circle(3))처럼 module명 생략 가능하다.
# 

# 다른 이름으로 치환하려면 as를 사용한다.
# import area as ar
# ar.circle(5)
# 함수의 경우도 동일하다.
# from area import circle as ci 
# ci(2) 
# 
# 
# from area import * 형식으로 사용가능지만 권장되지는 않는다.
#   

# 모듈은 여러 기능을 모아둔 파이썬 파일입니다.

"""

예를 들어 우리는 평면도형의 면적을 구해 주는 함수들을 모아서 area라는 모듈을 만들었습니다.

area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length
모듈은 파일 이름에서 .py 확장자를 빼고 부릅니다.

모듈 임포트(import)
모듈에 저장된 기능을 가져다 쓰기 위해서는 모듈을 임포트(import)하면 됩니다. 모듈을 임포트하는 방법은 여러 가지가 있습니다.

import <module>
모듈 전체를 임포트합니다. 모듈 안에 있는 변수 또는 함수는 .으로 접근할 수 있습니다.

run.py

import area

print(area.circle(2))
print(area.PI)
from <module> import <member(s)>
모듈에서 필요한 것들만 임포트합니다. 불러온 변수나 함수를 접근할 때 앞에 module.을 붙이지 않습니다.

run.py

from area import circle, square

print(circle(2))
print(square(3))
from <module> import *
모듈에서 모든 걸 임포트합니다.

run.py

from area import *

print(PI)
print(circle(2))
print(square(3))
그런데 이 임포트 방식을 사용하면 어떤 함수가 어떤 모듈에서 왔는지 알 수가 없고 자신도 모르게 쓸데없는 것들을 가져올 수 있습니다. 
그래서 이 방식은 파이썬 커뮤니티에서 권장하지 않는 방식입니다. 모듈을 사용할 때는 모듈을 그대로 가져오거나 모듈에서 필요한 것들만 가져오는 것을 추천드립니다.

as 키워드
임포트 문 뒤에 as라는 키워드(특별한 의미를 가지고 있는, 이미 예약된 문자열)를 붙여서 임포트하는 것의 이름을 바꿔줄 수 있습니다.

run.py

# 모듈 이름을 바꿈
import area as ar
print(ar.circle(2))

# 함수 이름을 바꿈 
from area import square as sq
print(sq(3))

"""




print(area.circle(5))
print(area.PI) 
print(area.squre(4))