a=input("Enter Your Email : ")
j=-1
for i in range(0,len(a)):
    if a[i] == '@':
        j=i
        break
Username=a[0:j]
Domain=a[j+1:len(a)]

print("Username : ",Username,"\nDomain : ",Domain)

"""
ALTERNATIVE METHOD
a=input("Enter your Email : ")
j=a.find('@')
if j == -1:
  print("Invalid Email Entered")
else:
  Username = a[0:j]
  Domain = a[j+1:]
print("Username : ",Username,"\nDomain : ",Domain)
"""