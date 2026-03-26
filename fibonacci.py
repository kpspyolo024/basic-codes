print("question: generate and print first n terms of fibonacci sequence where n is greater than equal to 1.")
n = int(input("enter the frequency:"))
a=0
b=1
i=2
if n==1:
  print(a)
elif n==2:
  print(a)
  print(b)
else:
  print(a)
  print(b)
  for i in range (n-2):
    c=a+b
    a=b
    b=c
  print(c)
