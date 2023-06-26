n= input("enter n")
mn = input("Enter mn")
mx = input("Enter mx")
if int(mn) == int(mx):
    print("it is not a range")
else:
    l = []
    for r in range(int(mn),int(mx)+1):
        if int(n)%int(r)==0:
            # l.append(f"{mn} is a divisor")
            print(f"{r} is a divisor")
            # mn = int(mn) + 1
        else:
            # l.append(f"{mn} is not a divisor")
            print(f"{r} is not a divisor")
            # mn = int(mn) + 1
        r = int(r) + 1
    # print(l)

