def anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("Yes")
    else:
        print("No")
s1=str(input())
s2=str(input())
anagram(s1,s2)