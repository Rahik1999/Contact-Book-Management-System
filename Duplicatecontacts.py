import addcontact as adc
phonenum=[]
phonenum.append(adc.phonenumber)
for i in range(0,len(phonenum)):
    for j in range(i+1,len(phonenum)):
        if j<len(phonenum) and (phonenum[i]==phonenum[j]):
            phonenum.pop(j)
        else:
            j=j+1
print(phonenum)
