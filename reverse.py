print("question: design an algorithm that accepts a positive integer and reverses the order of its digits.")
x=int(input("enter the number you want to reverse:"))
k=0
while x>0:
  j=x%10
  k=k*10+j
  x=int(x/10)
print("reverse order is:", k)
