f=open('C:\\Users\\MEGAPOLIS\\Desktop\\books.txt', encoding='utf8')
a=f.readlines()
shapka=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split('%')
    a[i][0] = int(a[i][0])
for x in a:
    x[5]=x[5].replace(',','.')
    x[5]=float(x[5])
shapka=shapka.strip().split('%')
a1=[]
d={}
for x in a:
    if x[2] not in a1:
        a1.append(x[2])
        d[x[2]]=1
    else:
        d[x[2]]+=1
k=0
e=[]
for j in range(15,0,-1):
    for x in a1:
        if int(d[x])==j and k!=10:
            print(x)
            e.append(x)
            k+=1
f=open('top_10_authors.csv','w', encoding='utf8')
f.writelines('authors\n')
for x in e:
    f.writelines((str(x))+'\n')
f.close()