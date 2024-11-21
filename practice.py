dict1={"name":"Progress","surname":"Murau"}
dict2={"age":"boy","height":"Lineage"}
y=zip(dict1.values(),dict2.values())
for i,j in y:
    print({i,"is ",j})