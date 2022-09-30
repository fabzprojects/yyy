from enum import unique
from ssl import _create_unverified_context
from onroad import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    location = db.Column(db.String(200),default='')
    address = db.Column(db.String(50),default='')
    hospital = db.Column(db.String(50),default='')
    date = db.Column(db.String(200))
    month = db.Column(db.String(200))
    year = db.Column(db.String(200))
   
    

    

class Bookings(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(200))
    aid= db.Column(db.String(200))
    uemail = db.Column(db.String(80))
    aemail = db.Column(db.String(80))
    uname = db.Column(db.String(200))
    aname = db.Column(db.String(200))
    ucontact = db.Column(db.String(200))
    acontact = db.Column(db.String(200))
    location = db.Column(db.String(200),default='')
    address = db.Column(db.String(50),default='')
    hospital = db.Column(db.String(50),default='')
    status=db.Column(db.String(200))
    accept=db.Column(db.String(200))
    reject=db.Column(db.String(200))
    dat=db.Column(db.String(200))
    month=db.Column(db.String(200))
    year=db.Column(db.String(200))




class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email= db.Column(db.VARCHAR)
    message= db.Column(db.String(200))
