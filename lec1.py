"""
 file 읽기 
"""

with open("sample.txt", "r") as f:
  for line in f:
    print(line)

"""
 strip : 앞 ,뒤의 white character(space포함)를 없애준다.
"""
with open("sample.txt", "r") as f:
  for line in f:
    print(line.strip())

"""
 split : return 값은 string type이다. 
 split()에 아무런 indeicator를 주지 않은 경우는 whitecharacter가 된다.
"""

name = "sangho,Hyun"
names = name.split(",")
first_name = names[0]
last_name = names[1]

print(first_name,last_name)

str = " \n\t 1 2 3 4 \t 5 "
strs = str.split()
print(strs[0],strs[2],strs[1]+strs[3])

"""
:의 왼쪽에는 해달 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.
data 폴더의 chicken.txt 파일을 읽어 들이고, 
strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요. 
평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 
이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.

"""

with open('chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)

"""
이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요. 
사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다.

사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다. 
사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.
"""

with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')    
        if english_word == 'q':
            break
        
        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == 'q':
            break
        
        f.write('{}: {}\n'.format(english_word, korean_word))


"""
앞선 실습 과제에서 vocabulary.txt라는 파일을 만들었죠? 
이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요. 
이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내 주는 프로그램을 만들려고 합니다.

프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 
사용자는 그에 맞는 영어 단어를 입력해야 합니다. 
사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 
틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.

문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.
"""

with open('vocabulary.txt', 'r') as q:
    for line in q:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        s
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))


  """
  지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요. 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.

이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.

같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.
  """

import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
