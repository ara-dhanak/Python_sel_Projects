#Ha = 2 Hb = 6
#Ha = 2*3 = 1way, addition, 2^2 + 2

#Maximum ways to find out height

inp = ['o',' ','m',' ','a',' ','ra']
op= "omara"
str1 = "2,2,0,7,9,6,0,0,0,9,1"
li = list(str1)
c = 0
for i in range(0,len(li)):
    if li[i] == 0:
        li.remove(i)
        c += 1
        print(li)
    else:
        continue
for i in range(c):
    li.append(0)

print(li)
        









