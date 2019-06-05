#median of 3 numbers
values=[]
no=[1,2,3]
for i in no:
    values.append(input("Enter value "+str(i)+"\n"))
values.sort()
print("The median is: "+values[1])
