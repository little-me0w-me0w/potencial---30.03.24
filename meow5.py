f=open('C:\\Users\\MEGAPOLIS\\Desktop\\books.txt', encoding='utf8')
a=f.readlines()
shapka=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split('%')
    a[i][0] = int(a[i][0])
for x in a:
    x[5]=x[5].replace(',','.')
    x[5]=(float(x[5]))
shapka=shapka.strip().split('%')
d={}
a1=[]
for x in a:
    if x[2] not in a1:
        a1.append(x[2])
for i in range(len(a)):
    isbn = a[i][1]
    author = a[i][2]
    year = a[i][3]
    title=a[i][4]
    rate=a[i][5]
    if isbn not in d:
        d[isbn]=[author,year,title,rate]
    else:
        pass
"""
выводим список книг с наивысшим рейтингом с 2000 по 2007 года

"""
mx2000=0
name2000=0
author2000=0
for x in a:
    if int(x[3])==2000:
        if x[5]>mx2000:
            mx2000=max(mx2000,x[5])
            name2000=x[4]
            author2000=x[2]
print("Год: 2000")
print(f'{author2000} {name2000} {mx2000}')
mx2001=0
name2001=0
author2001=0
for x in a:
    if int(x[3])==2001:
        if x[5]>mx2001:
            mx2001=max(mx2001,x[5])
            name2001=x[4]
            author2001=x[2]
print("Год: 2001")
print(f'{author2001} {name2001} {mx2001}')
mx2002=0
name2002=0
author2002=0
for x in a:
    if int(x[3])==2002:
        if x[5]>mx2002:
            mx2002=max(mx2002,x[5])
            name2002=x[4]
            author2002=x[2]
print("Год: 2002")
print(f'{author2002} {name2002} {mx2002}')
mx2003=0
name2003=0
author2003=0
for x in a:
    if int(x[3])==2003:
        if x[5]>mx2003:
            mx2003=max(mx2003,x[5])
            name2003=x[4]
            author2003=x[2]
print("Год: 2003")
print(f'{author2003} {name2003} {mx2003}')
mx2004=0
name2004=0
author2004=0
for x in a:
    if int(x[3])==2004:
        if x[5]>mx2004:
            mx2004=max(mx2004,x[5])
            name2004=x[4]
            author2004=x[2]
print("Год: 2004")
print(f'{author2004} {name2004} {mx2004}')
mx2005=0
name2005=0
author2005=0
for x in a:
    if int(x[3])==2005:
        if x[5]>mx2005:
            mx2005=max(mx2005,x[5])
            name2005=x[4]
            author2005=x[2]
print("Год: 2005")
print(f'{author2005} {name2005} {mx2005}')
mx2006=0
name2006=0
author2006=0
for x in a:
    if int(x[3])==2006:
        if x[5]>mx2006:
            mx2006=max(mx2006,x[5])
            name2006=x[4]
            author2006=x[2]
print("Год: 2006")
print(f'{author2006} {name2006} {mx2006}')
mx2007=0
name2007=0
author2007=0
for x in a:
    if int(x[3])==2007:
        if x[5]>mx2007:
            mx2007=max(mx2007,x[5])
            name2007=x[4]
            author2007=x[2]
print("Год: 2007")
print(f'{author2007} {name2007} {mx2007}')