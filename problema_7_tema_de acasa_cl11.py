v=[15266,1254,12277,5645,84653,4653,9563]
print('venitul saptamanal al interprinderei este :', sum(v))
print('media venitului zilnic este:', sum(v/7))
if v.index(max(v))==0:
    print('ziua in care s-a obtinut cel mai mare venit este luni')
elif v.index(max(v))==1:
    print('ziua in care s-a obtinut cel mai mare venit este marti')  
elif v.index(max(v))==2:
    print('ziua in care s-a obtinut cel mai mare venit este miercuri')
elif v.index(max(v))==3:
    print('ziua in care s-a obtinut cel mai mare venit este joi')  
elif v.index(max(v))==4:
    print('ziua in care s-a obtinut cel mai mare venit este vineri')   
elif v.index(max(v))==5:
    print('ziua in care s-a obtinut cel mai mare venit este sambata')  
elif v.index(max(v))==6:
    print('ziua in care s-a obtinut cel mai mare venit este duminica')
if v.index(min(v))==0:
    print('ziua in care s-a obtinut cel mai mic venit este luni')
elif v.index(min(v))==1:
    print('ziua in care s-a obtinut cel mai mic venit este marti')  
elif v.index(min(v))==2:
    print('ziua in care s-a obtinut cel mai mic venit este miercuri')
elif v.index(min(v))==3:
    print('ziua in care s-a obtinut cel mai mic venit este joi')  
elif v.index(min(v))==4:
    print('ziua in care s-a obtinut cel mai mic venit este vineri')   
elif v.index(min(v))==5:
    print('ziua in care s-a obtinut cel mai mic venit este sambata')  
elif v.index(min(v))==6:
    print('ziua in care s-a obtinut cel mai mic venit este duminica')