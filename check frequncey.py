test={'codingal':2,'is':2,'best':2,'for':2,'coding':1}

print("the original dictonary: " + str(test))
k=2
res=0
for key in test:
    if test[key]==k:
        res=res+1
print("requency of k is :--" + str(res))