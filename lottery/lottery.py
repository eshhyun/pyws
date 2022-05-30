from random import randint

def generate_numbers(numberCount):

    numList =[]
    while len(numList) < numberCount:
      num = randint(1,45)
      if num not in numList:
         numList.append(num)

    return numList
"""
일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
"""
def draw_winning_numbers():
  winning_numbers = generate_numbers(7)
  return sorted(winning_numbers[:6]) + winning_numbers[6:]

"""
파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
"""
def count_matching_numbers(srclist,targetlist):

    matchingCount = 0
    for n in srclist :
        if n in targetlist :
           matchingCount += 1
    
    return matchingCount 
  

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
