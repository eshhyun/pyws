"""
프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "가 출력됩니다. 
총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
정답을 맞히면 "축하합니다. *번 만에 숫자를 맞히셨습니다."가 출력되고 프로그램은 종료됩니다.
사용자가 입력한 수가 정답보다 작은 경우 "Up"이 출력되고, 입력한 수가 정답보다 큰 경우 "Down"이 출력됩니다.
정답이 틀렸으면 1번부터 다시 진행합니다. 
만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, "아쉽습니다. 정답은 *입니다."가 출력되고 프로그램은 종료됩니다.

"""

import random

ANSWER = random.randint(1, 20)
NUM_TRIES = 4

guess = -1
tries = 0


while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")


if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))

 