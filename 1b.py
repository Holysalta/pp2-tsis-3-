string = raw_input()
low=string.lower()
liststr=list(low)
lenstr=len(liststr)
for i in range(lenstr-1):
      for j in range(lenstr-i-1):
            if liststr[j]>liststr[j+1]:
                  liststr[j],liststr[j+1]=liststr[j+1],liststr[j]
new_str=""
for m in liststr:
  new_str +=m          
print(new_str)