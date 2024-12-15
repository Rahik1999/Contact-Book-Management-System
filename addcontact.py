
def addcontact():
    count = 0
    while True:
        if count<userinput:
            name=input()
            email=input()
            phonenumber=int(input())
            address=input()
        else:
            break
        count=count+1
        return f"{name}\n,{email}\n,{phonenumber}\n,{address}"
x=addcontact()
