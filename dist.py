from math import cos, asin, sqrt
from random import choice as rc
import requests as  rq
# def rn(): return round(rnq()*10,1)

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin... 
    #dist is in kms

def getadd(st):
    a=st.index('formatted_address') + 20 
    ax=a+1
    while st[ax]!="'":
        ax+=1 
    return st[a+1:ax] 

def rf(fn='add.txt'):
    d=[]
    l = ['robbery','dacoity','murder','fraud','Natural Disaster','kidnapping']
    # cr=['robbery , chain snatching etc have been reported','murders have been reported', 'murder and rape have been reported' , 'kidnapping was reported', 'violent protests have been reported','terrorist attacks have been reported']
    with open(fn,'r') as f:
        t=f.read() 
    # print(t.split('\n'))
    for c in t.split('\n'):
        la,lo= map(float,c.split(', ')) 
        a=rq.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+','.join(map(str,[la,lo]))+'&key=AIzaSyDzSvMXoweTezf51RINyMwtbiyOVTdqoiI')
        json = str(a.json())
        d.append({'lat':la,'lon':lo,'crime':rc(l),'address': getadd(json)}) 
        # print(c)
    with open('dataset.txt','a') as dt:
        # can be performed directly without saving to a file
        dt.write('[')
        for y in d:
            dt.write(str(y)+',')
        dt.write(']')
        
    return(d)
def marker():
    rf()
    data = '' 
    with open('dataset.txt','r') as f: 
        data = f.read() 
    
    data =  eval(data)

    marks =[]
    for d in data:
        temp = {'icon':'http://maps.google.com/mapfiles/kml/shapes/caution.png','lat':d['lat'],'lng':d['lon'],'infobox':'warning: this site is well known for: <b>'+d['crime']+'</b><br>Address: '+d['address']}
        marks.append(temp)
    return marks

# see 33
# marker()
# for i in rf()[:2]:
#     print(i)


