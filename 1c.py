l,r = map(int,input().split())
for num in range(l,r+1):
    if num%7==1 or num%7==2 or num%7==5:
        print (num, end=' ')
    


