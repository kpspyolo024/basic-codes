print("question: given n numbers, design an algorithm that adds these numbers and returns the resultant sum. assume n greater than or equal to 0.")
x=int(input("enter the count of numbers you want to add:"))
sum=0
while x>0:
  j=int(input("enter number:"))
  sum = sum+j
  x=x-1
print("sum is", sum)
