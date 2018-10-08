f=open("we.txt","r")
count=0
for line in f:
    for word in line:
        if(word!=" "):
            count=count+1
print(count)
