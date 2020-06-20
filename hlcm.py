a,b=map(int,input().split())

if (a>b):
  maximum = a
else:
  maximum = b
while (True):
  if (maximum % a == 0 and maximum % b ==0):
    break
  maximum=maximum+1

i = 1
while(i <=a and i <=b):
      if(a%i == 0 and b%i ==0):
            gcd =i
      i += 1

print(maximum+gcd)
      
