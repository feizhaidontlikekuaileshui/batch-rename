import os
import re
fni=open("ni","r")

fname=[]
fidc=[]

for line in fni:
    if line[0]=="\n":
        break
    reidc=re.search(r"[0-9]{18}",line)
    fidc.append(str(reidc.group()))
    rename=re.search(r"[\u4e00-\u9fa5]+?.*?[\u4e00-\u9fa5]+?.*?[\u4e00-\u9fa5]*.*?[\u4e00-\u9fa5]*.*?",line,re.S)
    fname.append((str(rename.group())).replace(" ",""))

#print(list(range(0,len(fidc)))

flist=os.listdir()
for ename in flist:
    for index in list(range(0,len(fidc))):
        if fname[index] in ename:
            cmd="rename \""+ename+"\" \""+fidc[index]+".jpg\""
            print(cmd)
            #os.system(cmd)
