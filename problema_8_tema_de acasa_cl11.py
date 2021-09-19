t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print('temperatura medie este:', sum(t/24))
print('maximul temperaturii este',max(t)'iar minimul temperaturii este', min(t))
for i in t:
    if i ==max(t):
        print('ora/orele la care s-a inregistrat temperatura maxima este:', t.index(i)+1)
for i in t:
    if i==min(t):
        print('ora/orele la care s-a inregistrat temperatura minim este', t.index(i)+1)
z1=0
for i in t:
    if i<0:
        z1+=1
print ('numarul de zile in care au fost inregistrate temperaturi de 0 grade ', z1)
z2=0
for i in t:
    if i>sum(t)/24:
print('numarul de zile in care au fost inregistrate temperaturi mai mari de media saptamanii este', z2)                