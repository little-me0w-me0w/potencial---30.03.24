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
print(a)
for x in a:
    if x[2] not in a1:
        a1.append(x[2])
while 1:
    author =input()
    if author == 'автор':
        break
    for x in a:
        f=1
        if author not in a1:
            f=0
        else:
            pass
    if f==0:
        print('Данного автора в этой библиотеке нет')
    for x in a:
        if a.count(author)>1:
            print(1)
        if x[2]==author:
            print(f'“{x[4]} - {x[1]} - {int(x[0])} - {x[5]}”')
