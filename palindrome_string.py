# Palindrome String 
"""
test = input()     #rar

string = ""
flag=0
for i in test: 
    string = i + string
    if (test==string): 
        print("YES")
        break
else:
    print("No")
   
check=test[::-1]
if(check==test):
    print("YES")
else:
    print("NO")
"""
"""
T=int(input())
string=""
for i in range(T):
    n=input()
    a=n[::-1]
    if(n==a):
        print("YES")
    else:
        print("NO")


"""
T=int(input())
for i in range(T):
    string=""
    n=input()
    for i in n:
        string=i+string
        print(string)
    if (n==string):
        print("YES")
    else:
        print("NO")
       
