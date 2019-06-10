#Number of even and odd numbers
numbers=[]
size=int(input("Enter size "))
for i in range(0,size):
    numbers.append(int(input("Enter number ")))
odd=0
even=0
for i in numbers:
    if(i%2==0): even=even+1
    else: odd=odd+1
print("Number of even numbers: ",even,"\n")
print("Number of odd numbers: ",odd,"\n")
