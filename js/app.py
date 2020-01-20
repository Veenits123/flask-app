from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask import Flask, request, render_template, request,redirect ,url_for
from flask_cors import CORS

import requests as rq
from setup import app
CORS(app)
from forms import Form
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'somekey'
GoogleMaps(app, key="AIzaSyDzSvMXoweTezf51RINyMwtbiyOVTdqoiI")

from dist import distance, getadd, rf,getadd
def marker():
    # rf()
    data = '' 
    with open('dataset.txt','r') as f: 
        data = f.read() 
    
    data =  eval(data)

    marks =[]
    for d in data:
        temp = {'icon':'http://maps.google.com/mapfiles/kml/shapes/caution.png','lat':d['lat'],'lng':d['lon'],'infobox':'warning: this site is well known for: <b>'+d['crime']+'</b><br>Address: '+d['address']}
        marks.append(temp)
    return marks

def adfco(xa):
    a=rq.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+','.join(map(str,[xa[0],xa[1]]))+'&key=AIzaSyDzSvMXoweTezf51RINyMwtbiyOVTdqoiI')
    json = str(a.json())
    return getadd(json)


@app.route('/')
def test_page():
    return render_template('index.html',x=1)


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    form = Form()
    
    na = request.args.get('name').split(",")

    xa=list(map(float,na))
    # 'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    #          'lat': 37.4419,
    #          'lng': -122.1419,
    #          'infobox': "<b>Hello World</b>"
    

    mrks =marker()
    if form.validate_on_submit():
        ad = adfco(xa)
        cr = form.fb.data 
        mr = {'icon': 'http://maps.google.com/mapfiles/kml/paddle/grn-circle.png','lat': xa[0]+0.000019,'lng': xa[1]+.000019,'infobox': 'warning this site is well known for <b>'+cr+'</b><br>'+ad}
        mrks.append(mr)
        # original database not updated


    warns = ['<b>WARNING YOU ARE WITHIN THRESHOLD RANGE OF THESE AREAS</b>']
    for m in mrks:
         d  = distance(*xa,m['lat'],m['lng'])* 1000 # 1000x = into meters
         if d<=1000 :
             warns.append(str(m['infobox']))
   
    INFO="<B>KEEP WALKIN ,YOU'RE IN SAFE REGION</B>"
    if len(warns)>1:
        INFO='<br><br><hr>'.join(warns)
    mymap = Map(identifier="view-side", varname="mymap",style="height:75%;width:100%;margin:0;", lat=na[0],  lng=na[1],zoom=15,markers=[{'icon': 'http://maps.google.com/mapfiles/kml/paddle/grn-circle.png','lat': na[0],'lng': na[1],'infobox': INFO}]+mrks )
    return render_template('wc.html',mymap=mymap,form=form)


#see 57