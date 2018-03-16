hold = []
sp = []
x= input()
data = map(int,input().split(" "))
for k in data:
    if k in hold:
        if k not in sp:
            sp.append(k)
    else:
        hold.append(k)
