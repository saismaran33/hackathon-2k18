#entering the input
print("Enter the password for checking")
a=input()
x=len(a)
if x>6:
    #determining the accepted length for the password
    if x<21:
        print("accepted length")
    else:
        print("reached more than MAXIMUM  limit")
        #determining whether the entered input has character or digit
q=0
for c in a:
    if c.isdigit():
        print("One of the char is digit")
        q=1
        break
        #specifying condition saying that the character should be present
if q==0:
    print("Numeric should be there")
b=0
while b==0:
    #determining the symbols and defining a condition saying that the entered password should contain symbols
    if '$' in a:
        print("done with symbol")
        break
    elif '@' in a:
        print("Symbol is present")
        break
    elif '!' in a:
        print("done with symbol")
        break
    elif '*' in a:
        print("done with symbol")
        break
    else:
        print("symbol is missing")
        break
        #checking for the lower case
r=0
for c in a:
    if c.islower():
        print("lowcase is avialble")
        r=1
        break
if r==0:
    print("use lower case")
s=0
for c in a:
    #checking for the UPPER CASE
    if c.isupper():
        print("UPPER CASE is available")
        s=1
        break
if s==0:
    print(" use UPPER CASE")