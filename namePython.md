name 특수 변수

name 이란?
__name__은 모듈의 이름을 저장해 놓은 변수입니다.

__name__의 값은 파이썬이 알아서 정해 주는데요.

파일을 직접 실행하면 __name__은 __main__으로 설정됩니다
파일을 임포트하면 __name__은 모듈 이름으로 설정됩니다.
예를 들어 area 파일에서 __name__을 아래처럼 출력해 보면:

area.py

print(__name__)
area 파일을 직접 실행할 경우 __main__이라고 나오고:

__main__
area 파일을 임포트할 경우 area라고 나오는 거죠:

area
if __name__ == '__main__'
__name__을 사용하면 파일이 직접 실행되냐 아니면 임포트되냐에 따라서 코드의 흐름을 제어할 수 있습니다.

파일이 직접 실행될 때만 실행하고 싶은 코드는 if __name__ == '__main__'이라는 조건문 안에 넣어주면 됩니다.

area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

if __name__ == '__main__':
     # circle 함수 테스트
    print(circle(2) == 12.56)
    print(circle(5) == 78.4)

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)

area 파일을 직접 실행시키면 파일의 __name__은 __main__이 되기 때문에 조건문 안에 있는 코드가 실행되지만 area 파일을 임포트하면 __name__은 area가 되기 때문에 조건문 안에 있는 코드가 실행되지 않습니다.

그럼 이제 area 파일을 모듈처럼 쓸 수도 있고 스크립트처럼 쓸 수도 있겠죠?

