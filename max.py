print("Question: finding maximum number in set of n numbers")
n=[3,7,3,295,34,103,45,23,10032,324,97,43]
print(n)
max=n[0]
g=len(n)
k=0
r=0
while k<g-1:
  if max<n[r+1]:
    max=n[r+1]
  r=r+1
  k=k+1
print("the maximum number is",max)
