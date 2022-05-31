
패키지는 모듈들을 모아 놓은 디렉토리를 뜻합니다.

예를 들어 우리는 평면도형의 면적을 구해 주는 area 모듈과 입체도형의 부피를 구해주는 volume 모듈을 모아서 
shapes라는 패키지를 만들었습니다. shapes 패키지의 구조는 아래와 같습니다.

shapes/
    __init__.py
    area.py
    volume.py

shapes/area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

shapes/volume.py

PI = 3.14

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius * radius

# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length

패키지는 일반 디렉토리와 똑같은데 안에 __init__.py라는 파일이 있습니다.

패키지 임포트
모듈과 비슷하게 패키지 안에 있는 내용을 가져올 때도 import 키워드를 사용합니다.

import <package.module>

run.py

import shapes.volume

print(shapes.volume.cube(3))
이렇게 패키지 안에 있는 모듈을 가져올 수 있습니다. 패키지나 모듈 안에 있는 것은 항상 . 을 이용해서 접근합니다.

import <package>

run.py

import shapes

print(shapes.volume.cube(3)) # 오류
이렇게 패키지 자체를 임포트할 수도 있는데 그러면 패키지 안에 있는 내용들은 임포트되지 않습니다 (패키지 안에 있는 모듈도 같이 임포트하려면 패키지의 init 파일을 활용해야 합니다 - 다음 레슨들 참고). 그래서 위 코드는 오류가 납니다.

참고로 import ... 방식을 써서는 모듈의 함수나 변수를 바로 가져올 수 없습니다.

run.py

import shapes.volume.cube # 오류
import ... 방식으로는 패키지나 모듈만 임포트할 수 있습니다.

from <package> import <module(s)>

run.py

from shapes import volume
print(volume.cube(3))
from ... import ... 방식도 패키지에 쓸 수 있습니다. 패키지 안의 모듈을 바로 가져올 수도 있고...

from <package.module> import <member(s)>
전처럼 모듈 안에 있는 변수나 함수를 가져올 수도 있습니다.

run.py

from shapes.volume import cube

print(cube(3))
as 키워드
그리고 임포트 문 뒤에 as 키워드를 써서 임포트하는 것의 이름을 바꿔줄 수 있습니다.

run.py

import shapes.volume as vol

print(vol.cube(3))
