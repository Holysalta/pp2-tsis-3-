num=int(input())
compare = num
rev_number = 0
while(num>0):
  dig = num % 10 
  rev_number =rev_number * 10 + dig
  num= num //10
if(compare==rev_number):
  print("YES")
else:
  print("NO")