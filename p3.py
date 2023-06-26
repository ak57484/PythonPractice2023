l= input("enter a list of numbers").split(",")
# l2 = l1.__reversed__()

l2= l.__reversed__()
print(l,'\n')
l3=[]
for n in l2:
    l3.append(n)

print(f"Third Reversed list is {l3}")


l4= l[::-1]
print(f"Third Reversed list is {l4}")


#
# print(type(l))
l5= l[:]
for i in range(len(l5)//2):
    l5[i], l5[len(l5) - i - 1] = l5[len(l5) - i - 1], l5[i]

print(f"Third Reversed list is {l5}")
