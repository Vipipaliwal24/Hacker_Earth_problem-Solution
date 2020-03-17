T=int(input())
for i in range(T):
    N=input()
    a=N[::-1]
    if(a==N):
        print("YES")
    else:
        print("NO")
