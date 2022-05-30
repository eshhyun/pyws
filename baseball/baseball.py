"""
규칙
컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. 

예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고 6, 7, 4를 뽑을 수도 있는 거죠.
사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.

컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
숫자의 값과 위치가 모두 일치하면 S입니다.
숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
예를 들어 컴퓨터가 1, 2, 3을 뽑았다고 가정합시다. 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.
3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다
"""

from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def take_guess():
    new_guess = []
    while len(new_guess) < 3:
        num = int(input("{}번째 수를 입력하세요: ".format(len(new_guess) + 1)))

        if num < 0 or num > 9:
            print("0에서 9까지의 수를 입력해 주세요!")
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))