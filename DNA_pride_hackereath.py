T=int(input())
for i in range(T):
    N=int(input())
    s=input().upper()

    if 'U' in s:
        print("Error RNA nucleobases found!")
    else:
        string=""
        for i in s:
            if(i=="A"):
                string=string+"T"
            elif(i=="T"):
                string=string+"A"
            elif(i=="G"):
                string=string+"C"
            elif(i=="C"):
                string=string+"G"
        print(string)
        
            

    
