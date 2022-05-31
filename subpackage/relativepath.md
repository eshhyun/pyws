상대 경로 임포트

임포트를 하는 곳의 위치를 기준으로 임포트하려는 것의 위치를 상대적으로 표현하는 걸 상대 경로 임포트라고 합니다. 
반대로 우리가 계속해 왔던 것처럼 임포트하려는 것의 경로를 다 풀어서 써 주는 것은 절대 경로 임포트라고 합니다.

상대 경로 임포트는 항상 . 아니면 ..으로 시작합니다. 
.은 현재 패키지 안을 뜻하고 
..은 상위 패키지 안을 뜻합니다. 
예를 들어 shapes 패키지의 init 파일의 기준으로는 현재 패키지가 mymath/shapes이고 상위 패키지는 mymath이겠죠?

그럼 상대 경로 임포트 예시를 몇 개 봅시다.

1. shapes 패키지의 init 파일에서 패키지 안에 있는 모듈들 가져오기:

mymath/shapes/__init__.py

# 절대 경로 임포트
from mymath.shapes import area, volume

# 상대 경로 임포트
from . import area, volume
훨씬 더 간결하죠? 임포트 문이 의미하는 것도 명확합니다: 현재 패키지에서 area, volume 모듈을 임포트 하라는 뜻입니다.

2. stats 패키지의 init 파일에서 패키지의 모듈들 안에 있는 함수들 모두 가져오기:

mymath/stats/__init__.py

# 절대 경로 임포트
from mymath.stats.average import * 
from mymath.stats.spread import *

# 상대 경로 임포트
from .average import *
from .spread import *

첫 번째 예시와 비슷하게 임포트 문이 더 간결해졌고 임포트 문이 의미하는 것도 명확합니다. 
현재 패키지의 average, spread 모듈에서 모든 내용을 다 가져오라는 뜻입니다.

3. area 모듈에서 average 모듈에 있는 data_mean 함수 가져오기 (프로그램을 만들다 보면 가끔 이렇게 패키지 안에서 다른 패키지에 있는 것이 필요할 때도 있습니다):

mymath/shapes/area.py

# 절대 경로 임포트
from mymath.stats.average import data_mean

# 상대 경로 임포트
from ..stats.average import data_mean
하지만 이번엔 상대 경로를 봐서는 average 모듈이 정확히 어디 있는지, 패키지 구조가 어떻게 되는지 파악하기가 힘듭니다. 상대 경로가 복잡해지는 경우 (주로 ..을 쓰는 경우)에는 그냥 절대 경로를 쓰는 것이 좋습니다.