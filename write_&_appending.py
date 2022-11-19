"""
f = open("file.txt", "a")
a=f.write("code with harry chutia hai \n")
print(a)
f.close()
"""

#f = open("file.txt", "a")
#a=f.write("code with harry chutia hai \n")
#print(a)
#f.close()

"""handle read & write both"""
f = open("file.txt","r+")
print(f.read())
f.write("thank you")
