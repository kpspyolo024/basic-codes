print("question: convert a decimal into its corresponding octal representation.")
n=int(input("enter the number:"))
k=0
while n>0:
  x=n%8
  k=k*10+x
  n=int(n/8) 
j=0
while k>0:
  o=k%10
  j=j*10+o
  k=int(k/10)
print(j)
