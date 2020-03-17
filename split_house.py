n=int(input())   # taking no of grid
Str=input()       # taking string

if("HH" in Str):             
    print("NO")
else:
    print("YES")
    print(Str.replace(".","B"))      # replace . with B
