"""
try:
    while True:
        s=list(input())
       
        i=0
        while(i<len(s)-1):
            if(s[i]=='/' and s[i+1]=='/'):
                break
            if(s[i]=='-' and s[i+1]==">"):
                s[i]='.'
                s.pop(i+1)
            i+=1
        print("".join(s))
except EOFError:
    pass
"""


s=list(input())
i=0
while(i<len(s)-1):
    if(s[i]=='/' and s[i+1]=='/'):
        break
    if(s[i]=='-' and s[i+1]==">"):
        s[i]='.'
        s.pop(i+1)
    i+=1
print("".join(s))
