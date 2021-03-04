#description of the problem
#무한히 큰 배열에 다음과 같이 분수들이 적혀있다.이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자. X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
#input
#첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
#output
#첫째 줄에 분수를 출력한다.

#풀이 과정
#본인은 대각선의 층을 나두고 패턴을 찾아서 공식을 세움
#다른 분들 효율적 코딩은 x-=n, n+=1해서 x<=n일 때를 찾고, n이 짝수이면x/n-x+1 홀수이면 반대.

#def fraction
def fraction(x) :
  layer=1
  while True :
    if x <= layer*(layer+1)/2 :
      break
    layer+=1
  if layer%2 :
    denomirator=int(layer-(layer*(layer+1)/2-x))
    numerator=int(layer*(layer+1)/2-x+1)
  elif not layer%2 :
    denomirator=int(layer*(layer+1)/2-x+1)
    numerator=int(layer-(layer*(layer+1)/2-x))
  return denomirator, numerator

#main
x=int(input())
denomirator, numerator = fraction(x)
print(numerator,"/",denomirator,sep="")