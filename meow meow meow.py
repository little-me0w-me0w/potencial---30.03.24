
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
mx1=0
name1=0
k1=0
author1=''
mx2=0
name2=0
k2=0
author2=''
mx3=0
name3=0
k3=0
author3=''
for i in range(len(a)):
    if a[i][5]>mx1:
        mx1=max(mx1,a[i][5])
        name1=a[i][4]
        k1=i
        author1=a[i][2]
for i in range(len(a)):
    if a[i][5]>mx2 and i!=k1:
        mx2=max(mx2,a[i][5])
        name2=a[i][4]
        k2=i
        author2=a[i][2]
for i in range(len(a)):
    if a[i][5]>mx3 and i!=k1 and i!=k2:
        mx3=max(mx3,a[i][5])
        name3=a[i][4]
        k3=i
        author3=a[i][2]
print(f'“{name1} - {author1} - {mx1}”')
print(f'“{name2} - {author2} - {mx2}”')
print(f'“{name3} - {author3} - {mx3}”')