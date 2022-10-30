dict = {}
#print(type(dict))
d2 ={"name":"vijay","class":"mca","institute":"poddar","other":{"n":"ram","c":"mca","i":"poddar"}}
#print(d2)
#print(d2["other"]["n"])
d2["anant"]="b.tech"
#d3=d2.copy()
#del d3["other"]
#print(d3)
#print(d2.get("anant"))
d2.update({"raju":"b.sc"})
print(d2)
print(d2.keys())
print(d2.items())
