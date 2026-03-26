print("question: design an algorithm to evaluate the function sin(x) as defined as a infinite series expansion.")
x=float(input("enter the value of x:"))
j=x
tsin=x
term=x
i=1
x2=x*x
err=10**-5
while abs(j)>err:
  i=i+2
  term=-(term*x2)/(i*(i-1))
  tsin=tsin+term
  j=j/10
print("value of sinx is", tsin)
