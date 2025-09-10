s1='aabb'
s2='aaba'
flag=False
if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1 == s2:
            flag=True
            break
        else:
            s2 = s2[1:]+s2[:1]
if flag:
    print("True")
else:
    print("False")