print("Insert string")
stng=input()
count=0
size=len(stng)

for char in stng:
  count=count+1
  if count==1:
    c1=char
  if count==2:
   c2=char
  if count==size-1:
    c3=char
  if count==size:
   c4=char

if size>1:
    str=c1+c2+c3+c4

    print(str)


