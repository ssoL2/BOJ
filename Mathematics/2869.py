#description of the problem
'''땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.'''
#input 
#첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
#output
#첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

#풀이과정
#처음에는 date=1부터 v를 초과할 때까지 찾는 코드를 짰는데 '시간 초과'
#계산해서 찾을 수 있는 것은 while 돌리지 말고 찾자!!!!!!!!!!!!!
#math.ceil 중요

import math

#def date_calculator
def date_calculator(a,b,v) :
  n=a-b
  a1=a
  return math.ceil(1+(v-a)/n)

#main
a,b,v=map(int, input().split())
print(date_calculator(a,b,v))