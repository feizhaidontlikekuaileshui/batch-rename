#coding=utf-8
import os
fl=open('idc.txt','w',encoding='utf-8')
fl.close()
os.system('idc.txt')
fl=open('idc.txt','r')
idcl=fl.readline()
idcl=idcl.replace(' ','')
idcl=idcl.replace('\t','')
while True:
    if not idcl[-1]=='\n':
        idcl=idcl+'\n'
    name=idcl[:-19]+'.jpg'
    idc=idcl[-19:-1]+'.jpg'
    print(name+'->'+idc,end='')
    try :
        os.rename(name,idc)
    except FileNotFoundError:
        print('#'*10+'失败')
        er=open('没有照片.txt','a',encoding='utf-8')
        er.write(name[:-4])
        er.write('  ')
        er.write(idc[:-4])
        er.write('\n')
        er.close()
    else:
        print('-'*6+'成功')
    idcl=fl.readline()
    idcl=idcl.replace(' ','')
    idcl=idcl.replace('\t','')
    if idcl=='':
        break
fl.close()
er=open('没有照片.txt','a',encoding='utf-8')
er.write('#'*15+'结束'+'#'*15+'\n')
er.close()
print('没有照片名单在 \'没有照片.jpg\'')
os.system('没有照片.txt')
input('完成')
