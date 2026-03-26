x=[4,5,6,7,3,8,67,45,783,2398,65,543,872,65]
print("question: to find the kth smallest element")
print("there are",len(x), "numbers in the list.")
k=int(input("enter the element position you want:"))
b=[]
min=x[0]
for j in range(k):
  for i in range(len(x)-1):
    if x[i]<min:
      min=x[i]
  b.append(min)
  x.remove(min)
  min=x[0]
print(b[k-1])
