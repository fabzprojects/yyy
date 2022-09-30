from msilib.schema import File
from flask import Flask, render_template, request, redirect,send_file,  flash, abort, url_for
from onroad import app,db,mail
from onroad import app,db,mail
from onroad import app
from onroad.models import *
from onroad.forms import *
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
import os
from datetime import datetime,date









@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/map')
def map():
    return render_template("map.html")



@app.route('/umap')
def umap():
    return render_template("umap.html")







@app.route('/user_index/<id>')
def user_index(id):
    return render_template("user_index.html")



@app.route('/user_profile/<id>', methods=["GET","POST"])
def user_profile(id):
    d=Login.query.filter_by(id=id).first()
    if request.method=="POST":
        d.name=request.form["name"]
        d.username=request.form["email"]
        d.contact=request.form["contact"]
        # d.password=request.form["password"]
        d.address=request.form["address"]

        db.session.commit()
        m = "Profile Updated Successfully"
        return render_template('user_profile.html',m=m,d=d)
    else:
        return render_template("user_profile.html",d=d)



@login_required
@app.route('/user_contact/<id>', methods = ['GET','POST'])
def user_contact(id):
    d=Login.query.filter_by(id=id).first()
 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        my_data = Contact(name=name, email=email,message=message)
        db.session.add(my_data) 
        db.session.commit()
        m="Message Sent Successfully.."
   
        return render_template('user_contact.html',m=m,d=d)
    else :
        return render_template("user_contact.html",d=d)



@login_required
@app.route('/admin_view_feedbacks',methods=["GET","POST"])
def admin_view_feedbacks():
    obj = Contact.query.all()
    return render_template("admin_view_feedbacks.html",obj=obj)

@login_required
@app.route('/ambulance_contact/<id>', methods = ['GET','POST'])
def ambulance_contact(id):
    d=Login.query.filter_by(id=id).first()
 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        my_data = Contact(name=name, email=email,message=message)
        db.session.add(my_data) 
        db.session.commit()
        m="Message Sent Successfully.."
   
        return render_template('ambulance_contact.html',m=m,d=d)
    else :
        return render_template("ambulance_contact.html",d=d)



@app.route('/ambulance_profile/<id>', methods=["GET","POST"])
def ambulance_profile(id):
    d=Login.query.filter_by(id=id).first()
    if request.method=="POST":
        d.name=request.form["name"]
        d.username=request.form["email"]
        d.contact=request.form["contact"]
        # d.password=request.form["password"]
        d.address=request.form["address"]
        d.location=request.form["location"]
        d.hospital=request.form["hospital"]
        db.session.commit()
        m = "Profile Updated Successfully"
        return render_template('ambulance_profile.html',m=m,d=d)

    return render_template("ambulance_profile.html",d=d)


@app.route('/ambulance_index/<id>')
def ambulance_index(id):
    return render_template("ambulance_index.html")



@app.route('/user_view_bookings/<int:id>', methods=["GET","POST"])
def user_view_bookings(id):
  
    search=request.args.get('search')
    if search:
        obj=Bookings.query.filter(Bookings.dat.contains(search)|Bookings.aname.contains(search)|Bookings.location.contains(search)|Bookings.address.contains(search)|Bookings.hospital.contains(search)  & Bookings.uid.contains("id"))
    else:
        obj = Bookings.query.filter_by(uid=id).all()
 
    return render_template("user_view_bookings.html",obj=obj)



@app.route('/book_search', methods=["GET","POST"])
def book_search():
  
    search=request.args.get('search')
    if search:
        obj=Bookings.query.filter(Bookings.dat.contains(search)|Bookings.aname.contains(search)|Bookings.location.contains(search)|Bookings.address.contains(search)|Bookings.hospital.contains(search)|Bookings.month.contains(search)|Bookings.year.contains(search)|Bookings.uid.contains(search) )
        return render_template("book_reports.html",obj=obj)
    else:
        d="No Results Found"
        return render_template("book_search.html",d=d)
    return render_template("book_search.html")




@app.route('/user_search', methods=["GET","POST"])
def user_search():
  
    search=request.args.get('search')
    if search:
        obj=Login.query.filter((Login.year.contains(search)|Login.month.contains(search)|Login.date.contains(search)|Login.name.contains(search)|Login.location.contains(search)|Login.address.contains(search)|Login.hospital.contains(search) )& Login.usertype.contains("user") )
        return render_template("user_reports.html",obj=obj)
    else:
        d="No Results Found"
        return render_template("user_search.html",d=d)
    return render_template("user_search.html")




@app.route('/amb_search', methods=["GET","POST"])
def amb_search():
  
    search=request.args.get('search')
    if search:
        obj=obj=Login.query.filter((Login.year.contains(search)|Login.month.contains(search)|Login.date.contains(search)|Login.name.contains(search)|Login.location.contains(search)|Login.address.contains(search)|Login.hospital.contains(search) )& Login.usertype.contains("ambulance") )
        return render_template("amb_reports.html",obj=obj)
    else:
        d="No Results Found"
        return render_template("amb_search.html",d=d)
    return render_template("amb_search.html")
        
 
    




@app.route('/ambulance_view_bookings/<int:id>', methods=["GET","POST"])
def ambulance_view_bookings(id):
  
    search=request.args.get('search')
    if search:
        obj=Bookings.query.filter(Bookings.dat.contains(search)|Bookings.uname.contains(search)|Bookings.uemail.contains(search)|Bookings.ucontact.contains(search) & Bookings.aid.contains("id"))
    else:
        obj = Bookings.query.filter_by(aid=id).all()
 
    return render_template("ambulance_view_bookings.html",obj=obj)




@app.route('/admin_view_bookings', methods=["GET","POST"])
def admin_view_bookings():
  
    search=request.args.get('search')
    if search:
        obj=Bookings.query.filter(Bookings.year.contains(search)|Bookings.month.contains(search)|Bookings.uname.contains(search)|Bookings.dat.contains(search)|Bookings.aname.contains(search)|Bookings.location.contains(search)|Bookings.address.contains(search)|Bookings.hospital.contains(search)  )
    else:
        obj = Bookings.query.all()
 
    return render_template("admin_view_bookings.html",obj=obj)



@app.route('/')
def index():
 
    return render_template("index.html")


@app.route('/user_view_hospitals')
def user_view_hospitals():
 
    return render_template("user_view_hospitals.html")


@app.route('/admin_index')
def admin_index():
 
    return render_template("admin_index.html")




@app.route('/forgot_password', methods=["GET","POST"])
def forgot_password():
    if request.method=="POST":
        email=request.form["email"]
        d=Login.query.filter_by(username=email).first()
        pass_mail(d.username,d.password)
        return redirect('/login')
    else:
        return render_template("forgot_password.html")


def pass_mail(email,password):
    msg = Message('Password ',
                  recipients=[email])
    msg.body = f'''Your Password is {password}  '''
    mail.send(msg)





def msg_sendmail(username,name,nam,contact):
    
    msg = Message('New User Booking',
                  recipients=[username])
    msg.body = f'''Emergency Booking.Name : {nam} .  Contact : {contact} . Location Link  {name}'''
    mail.send(msg)




@app.route('/alert/<int:id>', methods=["GET","POST"])
def alert(id):
    d=Login.query.filter_by(id=id).first()
    if request.method=="POST":
        nam=request.form['nam']
        ucontact=request.form['ucontact']
        name=request.form['name']
        uemail=request.form['uemail']
        uid=request.form['uid']
        d.status="Waiting For Confirmation"
        k=str(date.today())
        p = date.today()
        month=p.strftime("%B")
        year=p.year
        data=Bookings(uid=uid,month=month,year=year,aid=d.id,accept="Accept",reject="Reject",uname=nam,location=d.location,address=d.address,hospital=d.hospital,aname=d.name,uemail=uemail,aemail=d.username,ucontact=ucontact,acontact=d.contact,dat=k,status="Waiting For Confirmation")
        db.session.add(data)
        db.session.commit()
        msg_sendmail(d.username,name,nam,ucontact)
        return redirect('/user_view_ambulance/'+str(current_user.id))
    else:
        return render_template('alert.html',d=d)







@app.route('/login', methods=["GET","POST"])
def login():

   
    if request.method=="POST":
         username=request.form['username']
         password=request.form['password']
      
         ambulance=Login.query.filter_by(username=username,password=password, usertype= 'ambulance').first()
         user=Login.query.filter_by(username=username,password=password, usertype= 'user').first()
         admin=Login.query.filter_by(username=username,password=password, usertype= 'admin').first()
     
         if admin:
             login_user(admin)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/admin_index')
             
         if ambulance:
             login_user(ambulance)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/ambulance_index/'+str(ambulance.id))
     
         
         elif user:
             login_user(user)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/user_index/'+str(user.id)) 

         else:
             d="Invalid Username or Password!"
             return render_template("login.html",d=d)


    
    return render_template("login.html")

          


@app.route('/accept/<int:id>')
def accept(id):
    c= Bookings.query.get_or_404(id)
    c.accept = "Accepted"
    c.reject="Reject"
    c.status="Accepted"
    db.session.commit()
    a_sendmail(c.uemail)
    return redirect('/ambulance_view_bookings/'+str(c.aid))


@app.route('/reject/<int:id>')
def reject(id):
    c= Bookings.query.get_or_404(id)
    c.reject = 'Rejected'
    c.accept="Accept"
    c.status="Rejected"
    db.session.commit()
    r_sendmail(c.uemail)
    return redirect('/ambulance_view_bookings/'+str(c.aid))


def a_sendmail(email):
    
    msg = Message('Approved Successfully',
                  recipients=[email])
    msg.body = f''' Congratulations , Your  Booking is Accepted successfully... '''
    mail.send(msg)

def r_sendmail(email):
  
    msg = Message('Booking Rejected',
                  recipients=[email])
    msg.body = f''' Sorry , Your  Booking is rejected. '''
    mail.send(msg)







@app.route('/user_register',methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        d = date.today()
        month=d.strftime("%B")
        year=d.year
        dat = str(date.today())
        
        my_data1 = Login(name=name,date=dat,month=month,year=year,address=address,username=email,contact=contact,password=password,usertype="user")
     
        db.session.add(my_data1) 
        db.session.commit()
        d="Registered successfully! Please Login.."
        return render_template("user_register.html",d=d)
        
    else :
       
        return render_template("user_register.html")




@app.route('/amb_register',methods=['GET', 'POST'])
def amb_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        location = request.form['location']
        password = request.form['password']
        hospital = request.form['hospital']
        address = request.form['address']
        d = date.today()
        month=d.strftime("%B")
        year=d.year
        dat = str(date.today())
   
        my_data1 = Login(name=name,date=dat,month=month,year=year,username=email,location=location,contact=contact,password=password,usertype="ambulance",hospital=hospital,address=address)
    

   
        db.session.add(my_data1) 
        db.session.commit()
        d="Registered successfully! Please Login.."
        return render_template("amb_register.html",d=d)
        
    else :
        return render_template("amb_register.html")






@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')







@login_required
@app.route('/user_view_ambulance/<int:id>',methods=["GET","POST"])
def user_view_ambulance(id):
    d=Login.query.filter_by(id=id).first()
    search=request.args.get('search')
    if search:
        obj=Login.query.filter(Login.name.contains(search)|Login.location.contains(search)|Login.address.contains(search)|Login.hospital.contains(search) & Login.usertype.contains("ambulance") )
    else:
        obj = Login.query.filter_by(usertype="ambulance").all()
   
    return render_template("user_view_ambulance.html",obj=obj,d=d)








@login_required
@app.route('/admin_view_ambulances',methods=["GET","POST"])
def admin_view_ambulances():
 
    search=request.args.get('search')
    if search:
        obj=Login.query.filter((Login.year.contains(search)|Login.month.contains(search)|Login.date.contains(search)|Login.name.contains(search)|Login.location.contains(search)|Login.address.contains(search)|Login.hospital.contains(search) )& Login.usertype.contains("ambulance") )
    else:
        obj = Login.query.filter_by(usertype="ambulance").all()
   
    return render_template("admin_view_ambulances.html",obj=obj)








@login_required
@app.route('/admin_view_users',methods=["GET","POST"])
def admin_view_users():
 
    search=request.args.get('search')
    if search:
        obj=Login.query.filter((Login.year.contains(search)|Login.month.contains(search)|Login.date.contains(search)|Login.name.contains(search)|Login.address.contains(search)) & Login.usertype.contains("user") )
    else:
        obj = Login.query.filter_by(usertype="user").all()
   
    return render_template("admin_view_users.html",obj=obj)