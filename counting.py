print("question: given n number of students, make a count of number of students that passed the examination. a pass is awarded for all marks  of 50 and above.")
x=int(input("enter the number of students you want to examine:"))
count=0
while x>0:
  j=int(input("enter marks:"))
  if j>=50:
    count=count+1
  x=x-1
print("no. of students passed are:", count)
