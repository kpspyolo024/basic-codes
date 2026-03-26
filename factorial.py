print("question: give a number n. compute the factorial of that number.")
x=int(input("enter the factorial you want:"))
fact=1
while x>0:
  fact=fact*x
  x=x-1
print(fact)
