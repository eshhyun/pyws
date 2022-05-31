__init__ 파일이란?

패키지 안에는 __init__.py라는 파일이 있습니다. 
__init__.py 파일 (지금부터는 그냥 init 파일이라고 하겠습니다) 은 '이 폴더는 파이썬 패키지다'라고 말해 주는 파일입니다.

파이썬 3.3 이전 버전에서는 init 파일이 필수였습니다. 
디렉토리 안에 init 파일이 없으면 디렉토리가 패키지로 인식되지 않아서 패키지를 임포트할 수 없었습니다.

파이썬 3.3 이후 버전부터는 init 파일이 필수가 아니게 됐지만 
파이썬 하위 버전과의 호환성과 패키지의 명확성을 위해 항상 패키지 안에 init 파일을 만들어 주는 것을 권장 드립니다.

init은 'initialize'라는 단어를 줄인 건데요. 
initialize는 초기화를 뜻합니다. 우리가 처음으로 패키지나 패키지 안에 있는 어떤 것을 임포트하면 가장 먼저 패키지의 init 파일에 있는 코드가 실행됩니다.

__init__ 파일 활용하기
init 파일을 어떻게 활용하는지 정리해 봅시다.

__init__ 파일에서 임포트 사용하기

패키지를 임포트하면 기본적으로 패키지 안에 있는 내용은 임포트되지 않습니다. 
패키지를 임포트할 때 패키지 안에 있는 내용도 함께 임포트하고 싶다면 init 파일을 활용해야 합니다.

init 파일에 패키지와 함께 임포트하고 싶은 것들을 써 주면 됩니다.

shapes/__init__.py

from shapes import area, volume

그러면 이제 shapes 패키지를 임포트하면 area랑 volume 모듈도 임포트되겠죠? init 파일에서 임포트하는 것은 패키지 안으로 임포트된다고 생각하시면 됩니다. area랑 volume 모듈은 아래와 같이 접근할 수 있습니다.

run.py

import shapes

print(shapes.area.circle(2))
print(shapes.volume.sphere(2))
그리고 모듈 대신 모듈의 함수들을 직접 임포트할 수도 있습니다.

shapes/__init__.py

from shapes.area import circle, square
그러면 우리는 이 함수들을 아래와 같이 접근할 수 있습니다.

run.py

import shapes

print(shapes.circle(2))
print(shapes.square(3))
shapes 패키지 안에서 함수들을 직접 가져왔기 때문에 area를 건너뛸 수 있는 거죠. init 파일에서 임포트되는 것은 항상 package.으로 접근할 수 있습니다. 위 처럼 호출 방식을 바꿔주는 것은 유용하게 쓰일 때도 있습니다.

__init__ 파일에서 변수 정의하기
상수값 PI는 area 모듈에서도 쓰이고 volume 모듈에서도 쓰입니다. PI처럼 패키지에 있는 여러 모듈이 필요로 하는 것들은 각 모듈에서 정의하지 않고 패키지 안에서 한 번만 정의해 주는 게 좋습니다. 똑같은 걸 여러 번 정의하는 건 비효율적이고 실수로 하나를 잘 못 정의하면 프로그램에 오류가 나기 때문입니다.

PI를 패키지 안에서 한 번만 정의해 주려면 (즉 패키지 레벨에서 정의해 주려면) PI를 shapes 패키지의 init 파일에서 정의해 주면 됩니다.

shapes/__init__.py

PI = 3.14
그리고 패키지 안에 있는 모듈에서는 PI를 임포트하면 됩니다.

shapes/area.py

from shapes import PI

# 원의 면적을 구해 주는 함수
def circle(radius):
        ...
shapes/volume.py

from shapes import PI

# 구의 부피를 구해 주는 함수
def sphere(radius):
    ...
PI같은 상수뿐만이 아니라 여러 모듈에서 필요한 변수, 함수 또는 객체는 패키지의 init 파일에서 정의해 주는 게 좋습니다.

그리고 패키지의 init 파일에서 정의되는 것들은 패키지 밖에서도 사용할 수 있습니다.

run.py

# PI 직접 임포트
from shapes import PI

# 패키지 임포트 후 shapes. 으로 접근
import shapes
shapes.PI