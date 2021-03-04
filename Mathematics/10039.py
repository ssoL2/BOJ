#https://www.acmicpc.net/problem/10039

def average(grade) :
  return sum(grade)//5

grade=list()
for i in range(5) :
  x=int(input())
  if x<40 : x=40
  grade.append(x)
print(average(grade))