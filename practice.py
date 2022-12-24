f=open("pk.txt","w")
line= 1
while True:
    data=input(f"Enter line numer {line}" :)
    f.write(data + "\n")
    line= line+1
    ans=input("do you want to enter another line (Y/N):").lower()
    if ans!="y":
        break
f.close()