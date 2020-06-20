def trib(n):
   if n==0:
      return 0
   elif n ==1 or n ==2:
      return 1
   else:
      return trib(n-1)+trib(n-2)+trib(n-3)
n=int(input())     
print(trib(n))
