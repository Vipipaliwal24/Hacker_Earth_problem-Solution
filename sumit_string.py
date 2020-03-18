"""sT=int(input())
for i in range(T):
    L=[]
    s=input().lower()
    for j in s:
        L.append(ord(j))
    for i in range(0,len(L)-1):
        v=[]
        x=L[i]-L[i+1]
        if(x==1 or x==-1):
            v.append(abs(x))
        else:
                v.append(0)
    print(v)
    if 0 in v:
        print("NO")
    else:
        print("YES")

"""
for i in range(int(input())):
    s=input().lower()
    l=[]
    f=1
    for i in s:
        l.append(i)
    for i in range(len(s)-1):
        if((l[i]=='a' and l[i+1]=='z') or (l[i]=='z' and l[i+1]=='a')):
            continue
        if(abs(ord(l[i])-ord(l[i+1]))!= 1):
            f=0
            break
    if(f==1):
        print("YES")
    else:
        print("NO")
            
    
            
    

