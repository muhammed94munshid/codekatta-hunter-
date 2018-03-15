d=[]
l=[]
a=int(input())
for i in range(0,a):
    l.append(int(input()))


l.sort(reverse=True)
for i in l:
    d.append(str(i))
b=int("".join(d))
print (b)
