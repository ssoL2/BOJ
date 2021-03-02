#def N -> thickness
def honey(N) :
  thickness = 1
  last = 1
  plus = 6
  if N==1 :
    return 1
  while True :
    last += plus
    thickness += 1
    if N <= last :
      return thickness
    else :
      plus+=6
#input
N=int(input())
print(honey(N))

'''#input
find = int(input())
#6*num+1 looking for thickness
#k is sequence
k=0
for i in range(0,int(1000000000/6)) :
  if find <= 6*(i+k)+1 :
    num = i
    break
  if i==0 :
    continue
  elif i==1 :
    k+=1
    continue
  k+=i
#result=num+1
print(num+1)'''