#WAP to print the count of even and odd from 1 to 10 using while loopi=1
even=0
odd=0
i=1
while i<=10:
    if i%2 == 0:
        even = even+1
    else:
        odd=odd+1
    i = i+1
print("Even =",even)
print("odd =",odd)

