a = int(input())
c = 0
while a>=25 and a >0:
    a-=25
    c+=1
while a>=10 and a>0:
    a-=10
    c+=1
while a>=5 and a>0:
    a-=5
    c+=1
while a>=1 and a>0:
    a-=1
    c+=1
print(c)