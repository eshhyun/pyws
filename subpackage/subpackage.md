서브패키지란?

패키지 안에는 모듈도 있을 수 있고 다른 패키지들이 있을 수도 있습니다. 
우리는 패키지 안에 또 다른 패키지가 있을 때 안에 있는 패키지를 서브패키지라고 합니다.

예를 들어 우리는 mymath라는 패키지를 만들고 그 안에 shapes 패키지랑 stats라는 패키지를 넣어주었습니다. mymath 패키지의 구조는 아래와 같은데요.

mymath/
    shapes/
        __init__.py
        area.py
        volume.py
    stats/
        __init__.py
        average.py
        spread.py

mymath/shapes/area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

mymath/shapes/volume.py

PI = 3.14

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius * radius

# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length
mymath/stats/average.py

# 데이터의 평을 구해 주는 함수
def data_mean(data):
    return sum(data) / len(data)

# 데이터의 중앙값을 구해 주는 함수
def data_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        # 데이터 개수가 짝수면 중앙에 위치한 두 값의 평군을 구함
        # [a, b, c, d, e, f] -> median = (c+d) / 2
        return (data[n/2] + data[(n/2)-1]) / 2
    else:
        # [a, b, c, d, e] -> median = c
        return data[(n-1)/2]

mymath/stats/spread.py

# 데이터의 범위를 구해 주는 함수
def data_range(data):
    return max(data) - min(data)
따라서 shapes 패키지랑 stats 패키지는 서브패키지라고 할 수 있습니다.

서브패키지도 결국 패키지이기 때문에 우리가 지금까지 배운 임포트 방식들을 사용하면 됩니다. 그럼 모듈과 패키지 임포트를 총정리해 보겠습니다.


임포트 총정리

import ...
첫 번째 방식은 import ... 방식입니다.

run.py

# 패키지 임포트
import mymath

# 서브패키지 임포트
import mymath.shapes

# 모듈 임포트
import mymath.shapes.area

# 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없음 
import mymath.shapes.area.circle # 오류
그냥 import 뒤에 가져오고 싶은 모듈이나 패키지를 써 주면 됩니다. 하지만 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없습니다.

그리고 (서브)패키지를 임포트할 때는 (서브)패키지 안에서 임포트하고 싶은 걸 (서브)패키지의 init 파일에 적어줘야겠죠?

from ... import ...
두 번째 방식은 from ... import ... 방식입니다.

run.py

# 패키지 안에 있는 패키지 임포트
from mymath import shapes

# 패키지 안에 있는 모듈 임포트
from mymath.shapes import area

# 모듈 안에 있는 함수 임포트
from mymath.shapes.area import circle

# import 뒤에는 . 을 쓸 수 없음 
from mymath import shapes.area # 오류
from 뒤에는 모듈이나 패키지가 올 수 있습니다. import 뒤에는 모듈이나 패키지 안에서 가져오고 싶은 걸 써 줍니다. import 뒤에는 . 을 쓸 수 없습니다.

as 키워드
그리고 항상 임포트 문 뒤에 as 키워드를 써서 임포트하는 것의 이름을 바꿔줄 수 있습니다.
