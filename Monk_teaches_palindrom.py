for i in range(int(input())):
    s=input().lower()
    a=s[::-1]
    if(a==s):
        if(len(a)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
        
    else:
        print("NO")
