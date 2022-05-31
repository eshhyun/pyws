"""
cil 패키지의 init 파일에서 import *를 사용해서 utils 모듈의 모든 함수들과 
processing 모듈의 invert, merge함수들을 임포트해 주세요 (processing 모듈의 다른 함수들은 임포트되면 안됩니다).

"""
from cilpackage2.utils  import *
from cilpackage2.processing import * # processing module내 __all__로 invert와 merge만 정의 되어 있으므로 2개만 import 된다.

