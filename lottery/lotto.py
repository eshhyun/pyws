"""
로또는 주 1회씩 열립니다. 하지만 한 사람이 한 회차에 여러 번 참여할 수도 있습니다.

번호는 1부터 45까지 있는데요. 
주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 
그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.

당첨 액수는 아래 규칙에 따라 결정됩니다.

내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
"""


"""
이 함수는 파라미터로 정수 n을 받습니다. 
무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다.
"""

from random import randint

def generate_numbers(numberCount):

    numList =[]
    while len(numList) < numberCount:
      num = randint(1,45)
      if num not in numList:
         numList.append(num)

    return numList

print(generate_numbers(6))


"""
일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
"""
def draw_winning_numbers():

  '''
  winning_numbers = generate_number(6)
  winning_numbers.sort()


  while True:
    bonusNum = generate_number(1)
    if bonusNum[0] not in winning_numbers :
       winning_numbers.append(bonusNum[0])
       break
  
  return winning_numbers

  '''
  winning_numbers = generate_numbers(7)
  return sorted(winning_numbers[:6]) + winning_numbers[6:]






print(draw_winning_numbers())



"""
파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
"""
def count_matching_numbers(srclist,targetlist):

    matchingCount = 0
    for n in srclist :
        if n in targetlist :
           matchingCount += 1
    
    return matchingCount 
  
genList = generate_numbers(6)
winningList = draw_winning_numbers()
matchingCount = count_matching_numbers(genList,winningList)

print("in:{}  target:{}  matching:{}".format(genList,winningList,matchingCount))




"""
참가자의 당첨 금액을 리턴합니다. 
파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요. 
numbers는 당연히 번호 여섯 개를 담고 있고, winning_numbers는 보너스까지 해서 번호 7개를 담고 있겠죠?
"""
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))

  
  
  
  

