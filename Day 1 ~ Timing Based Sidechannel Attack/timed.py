import sys,time
password="djrocks"
input=sys.argv[1]
for i in range(len(password)):
    time.sleep(0.1)
    inplen=len(input)
    if(i>len(password) or i>=inplen or password[i]!=input[i]):
        sys.exit(0)
print("you passed ")