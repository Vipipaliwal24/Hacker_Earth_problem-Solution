"""
a=input()
b=input()
flag=1
for i in range(len(a)):
    if a[i]>b[i] or len(a)!=len(b):
        flag=0
        break
    if flag==1:
        print("YES")
        break
    else:
        print('NO')
"""
a=input()
b=input()

if(len(a)!=len(b)):
    print("NO")

else:
    result = "YES"
    for i in range(len(a)):
        if (a[i]    >   b[i]):
            result("NO")
    print(result)
            
"""
A=list(input())
B=list(input())
count=0
for i in range(len(A)):
    if i < len(B) and A[i] <= B[i]:
        continue
    else:
        count=1
        if count==1:
            print("YES")
        else:
            print("NO")
    
 """   
"""

# Python 3 implementation of above approach 

# check whether the first string can be 
# converted to the second string 
# by increasing the ASCII value of prefix 
# string of first string 
def find(s1, s2): 
        A = len(s1)           # length of two strings
	B = len(s2)
	if(A != B):            # If lengths are not equal 
		return False
	d = [0 for i in range(A)]      # store the difference of ASCII values
	d[0] = ord(s2[0]) - ord(s1[0])   # difference of first element 

	for i in range(1, A, 1):           # traverse through the string 
		if (s1[i] > s2[i]):
                    return False
                else:
                    d[i] = ord(s2[i]) - ord(s1[i])
                for i in range(A - 1):
                    if (d[i] < d[i + 1]): 
			return False
        return True

# Driver code 
if __name__ == '__main__': 
	
	# create two strings 
	s1 = input()
	s2 = input()

	# check whether the first string can 
	# be converted to the second string 
	if (find(s1, s2)): 
		print("Yes") 
	else: 
		print("No") 

"""
