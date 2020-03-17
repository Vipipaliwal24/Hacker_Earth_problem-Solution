T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    c=1
    for i in range(len(S)-1):
        if(S[i]==S[i+1]):
            continue
        else:
            c +=1
    print(c)
