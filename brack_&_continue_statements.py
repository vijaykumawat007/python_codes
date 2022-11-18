"""i = 0
while(i<10):
    print("ram", end=" hare")
    i = i+1 
"""
#i = 0
#while(True):
#    if i+1<5:
#        i = i+1
#        continue
#    print(i+1, end=" ")
#    if(i==15):
#        break;
#    i = i+1 

"""true==1""" """false==0"""

while(1):
    inp =int(input("enter a number\n"))
    if inp>100:
        print("congrats you have entered a number greater then 100")
        break
    else:
        print("trt again\n")
        continue
