print("given a randomly ordered array of n elements, partition the elements into 2 subsets such as one set has lesser than the given number and the other set has greater and equal to that number.")
arr=[3,4,76,34,876,43,78,32,987,54,76,70]
k=[]
l=[]
g=len(arr)
x=int(input("enter the value you want to partition with:"))
for i in range(1,g):
  if x>=arr[i-1]:
    k.append(arr[i-1])
  else:
    l.append(arr[i-1])
print(k)
print(l)
