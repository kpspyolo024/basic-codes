print("Question: remove all duplicates from an ordered array accordingly.")
n=[2,2,8,15,23,23,23,26,29,30,32,32]
print(n)
l=[]
for i in range(len(n)):
  if i==0:
    l.append(n[i])
  else:
    if n[i]!=n[i-1]:
      l.append(n[i])
print("the new list is", l)
