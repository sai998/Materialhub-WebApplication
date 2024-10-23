import datetime
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app1.models import *

memail = "materialhub2@gmail.com"
mpass = "tqmc avqy ablu arax"
def loginn(request):
    return render(request,"login_index.html")

def login_post(request):
    usr_name=request.POST['textfield']
    passwd=request.POST['passwd']
    data = login.objects.filter(user_name=usr_name,user_password=passwd)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg']="lin"
        if data.user_type =='admin':
            return redirect('/adminHome')
        elif data.user_type =='dealer':
            request.session['lid'] = data.id
            request.session['did']= dealers.objects.get(LOGIN=data.id).id
            return redirect('/dealer_home')
        elif data.user_type =='driver':
            request.session['lid'] = data.id
            request.session['dvid'] = drivers.objects.get(LOGIN=data.id).id
            return redirect('/driver_home')
        elif data.user_type =='client':
            request.session['lid'] = data.id
            request.session['cid'] = users.objects.get(LOGIN=data.id).id
            return redirect('/home')
        else:
          return HttpResponse("<script>alert('Invalid user...');window.location='/'</script>")
    else:

        return HttpResponse("<script>alert('Does not exist!');window.location='/'</script>")


def viewComplaint(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head']="VIEW COMPLAINTS"
    res = complaint.objects.all()
    return render(request, "admin/viewComplaint.html",{"data":res})


def complaintReplay(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"admin/complaintReplay.html",{"id":id})

def complaintReplay_post(request,id):
    Complaints = request.POST['compalint']
    complaint.objects.filter(id=id).update(replay=Complaints,replay_date=datetime.datetime.now())
    return HttpResponse("<script>alert('Ok..');window.location='/viewComplaint'</script>")

def dealer(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = dealers.objects.filter(LOGIN__user_type='pending')
    return render(request, "admin/dealer.html",{"data":data})

def dealerapprove(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = dealers.objects.filter(LOGIN__user_type='dealer')
    return render(request, "admin/dealerapprove.html",{"data":data})

def editMaterial(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = material.objects.get(id=id)
    return render(request, "admin/editMaterial.html",{"data":data,"id":id})

def editMaterial_post(request,id):
    try:
        Type = request.POST['type']
        Rate = request.POST['rate']
        Image = request.FILES['image']

        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")  # current time
        fs = FileSystemStorage()
        fs.save(r"C:\Users\saisa\PycharmProjects\materialhub\app1\static\\" + dt + '.jpg', Image)
        path = '/static/' + dt + '.jpg'

        material.objects.filter(id=id).update(material_rate=Rate, material_type=Type, material_image=path)
        return HttpResponse("<script>alert('Updated.....');</script>")
    except Exception as e:

        Type = request.POST['type']
        Rate = request.POST['rate']
        material.objects.filter(id=id).update(material_rate=Rate, material_type=Type,)
        return HttpResponse("<script>alert('Updated.....');window.location='/viewMaterial#contents'</script>")


def materialAdd(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request, "admin/MaterialAdd.html")

def materialAdd_post(request):
    Type=request.POST['type']
    Rate=request.POST['rate']
    Image=request.FILES['image']
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")          # current time
    fs = FileSystemStorage()
    fs.save(r"C:\Users\saisa\PycharmProjects\materialhub\app1\static\\"+dt+'.jpg',Image)
    path = '/static/'+dt+'.jpg'
    print(Type.lower())

    flg = 0

    if material.objects.filter(material_rate = Rate,material_type = Type).exists():
        return HttpResponse("<script>alert('Already existed...');window.location='/viewMaterial#contents'</script>")
    a = material.objects.all()
    for i in a:
        if i.material_type.lower() == str(Type).lower():
            flg = flg + 1

    if flg == 1:
        return HttpResponse("<script>alert('Already existed...');window.location='/viewMaterial#contents'</script>")

    else:
        obj = material()
        obj.material_rate = Rate
        obj.material_type = Type
        obj.material_image = path
        obj.save()
        return HttpResponse("<script>alert('Added Successfully...');window.location='/viewMaterial#contents'</script>")


def viewFeedback(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    feedback_res = feedback.objects.all()
    #dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return render(request, "admin/viewFeedback.html",{"data":feedback_res,})



def viewMaterial(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    material_res = material.objects.all()
    return render(request, "admin/viewMaterial.html",{"data":material_res})

def viewRegisteredUser(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    regiUser_res = users.objects.all()
    return render(request, "admin/viewRegisteredUser.html",{"data":regiUser_res})

def adminHome(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"admin/admin_index.html")

def delete_material(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    material.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted...');window.location='/viewMaterial#contents'</script>")

def approve(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    login.objects.filter(id=id).update(user_type='dealer')
    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = login.objects.get(id=id).user_name
        msg['Subject'] = "Your MaterialHub Account is Activated!"
        body = "Dear "+str(login.objects.get(id=id).user_name)+",\n  Great news! Your account has been successfully activated. You can now log in and start exploring everything MaterialHub has to offer."
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
    except:
        pass


    return HttpResponse("<script>alert('Approved..');window.location='/adminHome'</script>")

def reject(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    login.objects.filter(id=id).update(user_type='reject')
    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = login.objects.get(id=id).user_name
        msg['Subject'] = "Your MaterialHub Account Activation Request"
        body = "Dear"+str(login.objects.get(id=id).user_name)+" ,\n Thank you for registering with MaterialHub. Unfortunately, we were unable to approve your account activation at this time. This could be due to incomplete information or other verification issues."
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
    except:
        pass
    return HttpResponse("<script>alert('Rejected..');window.location='/adminHome'</script>")

#Dealer...........

def register(request):
    return render(request,"dealer/Register_index.html")

def register_post(request):
    Dealer_name = request.POST['name']
    Email = request.POST['email']
    Phone = request.POST['phone']
    License = request.POST['license']
    Latitude = request.POST['latitude']
    Longitude = request.POST['longitude']
    Password = request.POST['passwd']
    if login.objects.filter(user_name=Email).exists():
        return HttpResponse("<script>alert('Email already existed....');window.location = '/register'</script>")
    elif dealers.objects.filter(license_no=License).exists():
        return HttpResponse("<script>alert('License already existed....');window.location = '/register'</script>")

    passd = login()
    passd.user_name = Email
    passd.user_password = Password
    passd.user_type = 'pending'

    passd.save()

    obj = dealers()
    obj.dealer_name = Dealer_name
    obj.phone_number = Phone
    obj.email = Email
    obj.longitude = Longitude
    obj.latitude = Latitude
    obj.license_no = License
    obj.LOGIN = passd


    obj.save()


    return HttpResponse("<script>alert('Registration Successful....');window.location = '/'</script>")

def driver_add(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    return render(request,"dealer/Add_driver.html")

def driver_add_post(request):
    name = request.POST['driver_name']
    email = request.POST['driver_mail']
    license = request.POST['licence']
    phn = request.POST['driver_phn']
    house = request.POST['house_name']
    place = request.POST['place']
    post = request.POST['post_addr']
    pin = request.POST['pin']

    p = random.randint(11111,999999)

    if login.objects.filter(user_name=email).exists():
        return HttpResponse("<script>alert('Email already exist....');window.location = '/addDriver#contents'</script>")
    elif drivers.objects.filter(license_no=license).exists():
        return HttpResponse("<script>alert('License already exist....');window.location = '/addDriver'</script>")

    passd = login()
    passd.user_name = email
    passd.user_password = p
    passd.user_type = 'driver'

    passd.save()


    obj = drivers()
    obj.driver_name = name
    obj.license_no = license
    obj.email = email
    obj.phone_no = phn
    obj.house_name = house
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.LOGIN = passd
    obj.DEALER = dealers.objects.get(LOGIN=request.session['lid'])
    obj.save()
    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = email
        msg['Subject'] = "Your MaterialHub Account Password"
        body = "Dear "+str(name)+",\n Welcome to MaterialHub! Below are the login details for your account: Password: "+ str(p)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
    except:
        pass


    return HttpResponse("<script>alert('Driver Added Successfull...');window.location='/dealer_home'</script>")




def edit_driver(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/view_drivers#contents'</script>")
    request.session['head'] = ""
    data = drivers.objects.get(id = id)
    return render(request,"dealer/Edit_Driver.html",{'view':data,'id':id})


def edit_driver_post(request,id):

        name = request.POST['driver_name']
        phn = request.POST['phone_number']
        house = request.POST['house_name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']

        drivers.objects.filter(id=id).update(driver_name=name,phone_no=phn,house_name=house,place=place,post=post,pin=pin)



        return HttpResponse("<script>alert('Details Updated...');window.location='/view_driver'</script>")


def update_stock(request,id,mid):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/view_material#contents'</script>")
    return render(request,"dealer/update_Stock.html",{'id':id,"mid":mid})

def update_stock_post(request,id,mid):
    stock_update = request.POST['updateStock']
    #print(id,"iddddddddd")
    if id=="0":
        obj = stock()
        obj.stock = stock_update
        obj.DEALER_id = request.session['did']
        obj.MATERIAL_id = mid
        obj.save()
    else:
        tt=stock.objects.get(id=id).stock
        total=int(stock_update)+int(tt)
        stock.objects.filter(id=id).update(stock=total)
    return HttpResponse("<script>alert('Stock updated...');window.location='/view_material#contents'</script>")



def view_driver(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    driver_lst = drivers.objects.filter(DEALER__LOGIN=request.session['lid'])
    return render(request,"dealer/view_Driver.html",{"data":driver_lst})

def view_material(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    res=material.objects.all()
    ar=[]
    for i in res:
        x=stock.objects.filter(MATERIAL_id=i.id,DEALER__LOGIN=request.session['lid'])
        if x.exists():
            ar.append({
                "stock":x[0].stock,
                "type":i.material_type,
                "image":i.material_image,
                "rate":i.material_rate,
                "s_id":x[0].id,
                "m_id":i.id
            })
            print(ar,"frst")
        else:
            ar.append({
                "stock":0,
                "s_id": 0,
                "type": i.material_type,
                "image": i.material_image,
                "rate": i.material_rate,
                "m_id":i.id
            })
            print(ar,"second")

    return render(request,'dealer/view_Material.html',{'data':ar})


def view_order(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = "USER REQUEST"
    data = order.objects.filter(status__in=["Online","Offline","Delivered"])
    new_data = []
    for i in data:
        if order_sub.objects.filter(ORDER=i.id,STOCK__DEALER__LOGIN=request.session['lid']).exists():

            x =  order_allocation.objects.filter(ORDER = i.id)
            if x.exists():
                i.DRIVER = x[0].DRIVER
                new_data.append(i)
            else:
                i.DRIVER = 'pending'
                new_data.append(i)

    return render(request,"dealer/view_Orders.html",{"data":new_data})

def allocate_driver(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = drivers.objects.filter(DEALER__LOGIN=request.session['lid'])
    return render(request,"dealer/allocate_Driver.html",{'data':data,"oid":id})


def driver_allocation(request,id,oid):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    date = datetime.datetime.now().date()

    if order_allocation.objects.filter(ORDER=oid).exists():
        return HttpResponse("<script>alert('Already Allocated...');window.location='/view_order'</script>")

    obj = order_allocation()
    obj.allocation_date=date
    obj.ORDER_id =oid
    obj.DRIVER_id=id
    obj.save()
    return HttpResponse("<script>alert('Allocated...');window.location='/view_order#contents'</script>")


def view_order_sub(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    data = order_sub.objects.filter(ORDER=id)
    return render(request,"dealer/view_Order_sub.html",{"data":data})

def userInfo_view(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    data = users.objects.get(id=id)
    return render(request,"dealer/userInfo_view.html",{"data":data})


def profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")

    a = dealers.objects.get(LOGIN=request.session['lid'])
    return render(request,"dealer/view_Profile.html",{'data':a})

def view_reviews(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    user = dealers.objects.get(LOGIN=request.session['lid'])
    did = user.id
    data = review.objects.filter(DEALER=did)
    return render(request,"dealer/view_Reviews.html",{'view':data})

def dealer_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"dealer/home_index.html")

def view_payment(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    data = payment.objects.filter()
    new_data = []
    for i in data:
        if order_sub.objects.filter(ORDER=i.ORDER_id , STOCK__DEALER=request.session['did']).exists():
            new_data.append(i)
    return render(request,"dealer/viewPayment.html",{"data":new_data})

def report(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    request.session['head'] = ""
    user = dealers.objects.get(LOGIN=request.session['lid'])
    data = payment.objects.filter()
    new_data = []
    new_date =[]
    new_amount =[]
    total = 0
    for i in data:
        if order_sub.objects.filter(ORDER=i.ORDER_id,STOCK__DEALER=user).exists():

                new_date.append(i.payment_date)
                new_amount.append(i.ammount)

    for i in range(0,len(new_date)):
        new_data.append({
            "payment_date":new_date[i],
            "ammount":new_amount[i]
        })
        total += int(new_amount[i])
    return render(request,"dealer/report.html",{"data":new_data,"t":total})

def search_post(request):
    user = dealers.objects.get(LOGIN=request.session['lid'])
    data = payment.objects.filter(payment_date=request.POST['search'])
    new_data = []
    new_date = []
    new_amount = []
    total = 0
    for i in data:
        if order_sub.objects.filter(ORDER=i.ORDER_id, STOCK__DEALER=user).exists():
            new_date.append(i.payment_date)
            new_amount.append(i.ammount)

    for i in range(0, len(new_date)):
        new_data.append({
            "payment_date": new_date[i],
            "ammount": new_amount[i]
        })
        total += int(new_amount[i])
    return render(request, "dealer/report.html", {"data": new_data, "t": total})

def delete_driver(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    l = drivers.objects.get(id=id)
    login.objects.get(id=l.LOGIN_id).delete()
    l.delete()
    return HttpResponse("<script>alert('Driver Deleted Successfull.....');window.location='/view_driver#contents'</script>")



#...............................Driver


def driver_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"driver/driver_indexhome.html")

def view_allocated_order(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = order_allocation.objects.filter(DRIVER=request.session['dvid'])
    return render(request,"driver/view_allocated_orders.html",{"data":data})


def item(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = order_sub.objects.filter(ORDER_id=id)
    return render(request,"driver/ITEM.html",{'data':data})

def payments(request,oid,uid):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = order.objects.get(id = oid).total_price
    return render(request,"driver/payment.html",{"uid":uid,"oid":oid,"a":a})

def payment_post(request,oid,uid):

    request.session['oid'] = oid
    p = str(random.randint(1111,9999))
    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = order.objects.get(id=oid).USER.user_email
        msg['Subject'] = "Your MaterialHub OTP Code"
        body = "Your OTP Code: " + p
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)

    except:
        pass
    order.objects.filter(id=oid).update(otp=p)
    return HttpResponse("<script>alert('Enter OTP');window.location='/otp#contents'</script>")

def driver_profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = drivers.objects.get(LOGIN=request.session['lid'])
    return render(request,"driver/viewProfile.html",{'data':a})


def otp(request):
    return render(request,"client/otp.html")

def otp_post(request):
    otp = request.POST['otp']
    oid = request.session['oid']
    q = order.objects.filter(id=request.session['oid'],otp=otp)
    if q.exists():
        obj = payment()
        obj.payment_date = datetime.datetime.now().date()
        obj.ammount = order.objects.get(id=oid).total_price
        obj.ORDER_id = oid
        obj.USER_id = order.objects.get(id=oid).USER_id
        obj.save()
        order.objects.filter(id=oid).update(status = 'Delivered')
        return HttpResponse("<script>alert('Completed...');window.location='/view_allocated_order#contents'</script>")
    else:
        return HttpResponse("<script>alert('Failed...');window.location='/otp#contents'</script>")

def otp2(request,oid,uid):
    p = str(random.randint(1111,9999))
    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = order.objects.get(id = oid).USER.user_email
        msg['Subject'] = "Your MaterialHub OTP Code"
        body = "Your OTP Code: " + p
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        order.objects.filter(id=oid).update(otp=p)
    except:
        pass


    return render(request,"driver/otp2.html",{"oid":oid,"uid":uid})

def otp2_post(request,oid,uid):
    otp2 = request.POST['otp2']
    q = order.objects.filter(id=oid, otp=otp2)
    if q.exists():
        order.objects.filter(id=oid).update(status='Delivered')
        return HttpResponse("<script>alert('Completed...');window.location='/view_allocated_order#contents'</script>")
    else:
        return HttpResponse("<script>alert('Failed...');window.location='/otp2#contents'</script>")





#----------------------------Client

def client_register(request):
    return render(request,"client/RegisterClient_index.html")
def home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")

    return render(request,"client/home_index.html")

def client_register_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phn = request.POST['textfield3']
    house = request.POST['textfield4']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    password = request.POST['textfield8']

    if login.objects.filter(user_name=email).exists():
        return HttpResponse("<script>alert('Email already existed....');window.location ='/client_register'</script>")

    psswd = login()
    psswd.user_name = email
    psswd.user_password = password
    psswd.user_type = 'client'

    psswd.save()
    obj = users()
    obj.user_name = name
    obj.user_email = email
    obj.house_name = house
    obj.place = place
    obj.pin = pin
    obj.post = post
    obj.user_phone = phn
    obj.LOGIN = psswd
    obj.save()

    try:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(memail, mpass)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = memail
        msg['To'] = email
        msg['Subject'] = "Your MaterialHub Account Is Successfully Registerd."
        body = "Dear "+str(name)+",\n Welcome to MaterialHub! Your MaterialHub Account Is Successfully Registerd. Thankyou for join us. "
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
    except:
        pass
    return HttpResponse("<script>alert('Registration Compleated...');window.location='/client_register'</script>")

def client_view_profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = users.objects.get(LOGIN=request.session['lid'])
    return render(request,"client/view_profile.html",{"data":a})


def client_view_material(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = material.objects.all()
    return render(request,"client/view_Materials.html",{"data":a})


def client_view_dealears(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = stock.objects.filter(MATERIAL=id)
    return render(request,"client/view_dealers.html",{"data":a})

def view_dealerReview(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = review.objects.filter(DEALER_id=id)
    return render(request,"client/view_Review.html",{"data":data})

def quantity_request(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    qty = stock.objects.get(id = id).stock
    return render(request,"client/quantity_request.html",{'id':id,"s":qty})

def quantity_req_post(request,id):
    qua = request.POST['qua']
    res=stock.objects.get(id=id).MATERIAL
    r=res.material_rate
    S=int(r)*int(qua)

    d=datetime.datetime.now()

    x = order.objects.filter(USER_id = request.session['cid'],status = "pending")
    # for checking user has pending order
    if x.exists():
        xx = order_sub.objects.filter(ORDER=x[0].id)
        # for getting item details
        if xx.exists():
            # selecting dealer info for checking if same dealer for material
            dealer_id = xx[0].STOCK.DEALER.id
            selectteddealer_id = stock.objects.get(id=id).DEALER_id

            if str(dealer_id) == str(selectteddealer_id):

                current_amount = int(x[0].total_price) + int(S)

                order.objects.filter(id = x[0].id).update(total_price = current_amount)

                obj = order_sub()
                obj.quantity = qua
                obj.STOCK_id = id
                obj.ORDER_id = x[0].id
                obj.save()
                print(obj.id)
            else:
                obj1 = order()
                obj1.order_date = d
                obj1.total_price = S
                obj1.USER_id = request.session['cid']
                obj1.otp = "pending"
                obj1.status = "pending"
                obj1.save()

                obj = order_sub()
                obj.quantity = qua
                obj.STOCK_id = id
                obj.ORDER_id = obj1.id
                obj.save()
                print(obj.id)

    else:
        obj1 = order()
        obj1.order_date = d
        obj1.total_price = S
        obj1.USER_id = request.session['cid']
        obj1.otp = "pending"
        obj1.status = "pending"
        obj1.save()

        obj = order_sub()
        obj.quantity = qua
        obj.STOCK_id = id
        obj.ORDER_id = obj1.id
        obj.save()
        print(obj.id)

    return HttpResponse("<script>alert('Successfully Added..');window.location='/client_view_material#contents'</script>")

def remove(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    totalprice  = int(order_sub.objects.get(id=id).ORDER.total_price)
    mprice  = int(order_sub.objects.get(id=id).quantity) * int(order_sub.objects.get(id=id).STOCK.MATERIAL.material_rate)
    order.objects.filter(id = order_sub.objects.get(id=id).ORDER.id).update(total_price = totalprice - mprice)
    oid = order_sub.objects.get(id=id).ORDER.id
    order_sub.objects.get(id=id).delete()
    if order_sub.objects.filter(ORDER=oid).exists():
        return HttpResponse(
            "<script>alert('Removed...');window.location='/view_requested_item/" + str(oid) + "'</script>")

    else:
        order.objects.get(id=oid).delete()
        return HttpResponse("<script>alert('Removed...');window.location='/view_request_status'</script>")



def send_complaint(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"client/send_complaint.html")

def compalint_Post(request):
    com = request.POST['complaints']
    obj = complaint()
    obj.complaint = com
    obj.complaint_date = datetime.datetime.now()
    obj.USER_id = request.session['cid']
    obj.replay = 'pending'
    obj.save()
    return HttpResponse("<script>alert('Submited..');window.location='/send_complaint'</script>")

def view_Replay(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    a = complaint.objects.filter(USER=request.session['cid'])
    return render(request,"client/View_replay.html",{"data":a})

def remove_replay(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    complaint.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed..');window.location='/send_complaint'</script>")


def send_feedBack(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"client/send_feedback.html")

def feedback_post(request):
    feedbk = request.POST['feedback']
    obj = feedback()
    obj.feedback = feedbk
    obj.feedback_date = datetime.datetime.now()
    obj.USER_id = request.session['cid']
    obj.save()
    return HttpResponse("<script>alert('Submited..');window.location='/home'</script>")

def send_Review(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    return render(request,"client/send_review.html",{"data":id})

def send_Review_post(request,id):
    reviews = request.POST['Review']
    obj = review()
    obj.review = reviews
    obj.review_date = datetime.datetime.now()
    obj.USER_id = request.session['cid']
    obj.DEALER_id = request.session['did']
    obj.save()
    return HttpResponse("<script>alert('Submited..');window.location='/view_request_status'</script>")


def view_request_status(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = order.objects.filter(USER=request.session['cid'])
    for i in data:
        totalprice = 0
        try:
            if i.status == 'pending':
                i.DEALER = order_sub.objects.filter(ORDER=i.id)[0].STOCK.DEALER

                data2 = order_sub.objects.filter(ORDER_id=i.id)
                count = len(data2)
                scount = 0
                for ij in data2:
                    if int(ij.quantity) > int(ij.STOCK.stock):
                        scount = scount + 1
                    else:
                        totalprice += int(ij.quantity) * int(ij.STOCK.MATERIAL.material_rate)
                if scount == count:
                    i.stockcount = "1"
                else:
                    i.stockcount = "0"
                i.total_price = totalprice
            else:
                i.DEALER = order_sub.objects.filter(ORDER=i.id)[0].STOCK.DEALER

                data2 = order_sub.objects.filter(ORDER_id=i.id)
                count = len(data2)
                scount = 0
                for ij in data2:
                    if int(ij.quantity) > int(ij.STOCK.stock):
                        scount = scount + 1
                    else:
                        totalprice += int(ij.quantity) * int(ij.STOCK.MATERIAL.material_rate)
                if scount == count:
                    i.stockcount = "1"
                else:
                    i.stockcount = "0"

        except Exception as e:
            print(e,"oooo")
            pass


    return render(request,"client/view_request_status.html",{"data":data})

def view_requested_item(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    data = order_sub.objects.filter(ORDER_id=id)
    for i in data:
       if i.ORDER.status == 'pending':
           i.amount = int(i.STOCK.MATERIAL.material_rate) * int(i.quantity)
           if int(i.quantity) > int(i.STOCK.stock):
               i.stockstatus = "1"
           else:
               i.stockstatus = "0"
       else:
           i.amount = int(i.STOCK.MATERIAL.material_rate) * int(i.quantity)

           i.stockstatus = "0"
    return render(request,"client/view_requested_items.html",{"data":data})

def cancel(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please login');window.location='/'</script>")
    order.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Canceled..');window.location='/view_request_status#contents'</script>")

def change_password(request):
    return render(request,"client/passwd.html")

def change_psswd_post(request):
    old = request.POST['textfield']
    nw = request.POST['textfield2']
    cnfrm = request.POST['textfield3']
    res=login.objects.filter(user_password=old,id=request.session['lid'])
    if res.exists():
        if nw == cnfrm:
            login.objects.filter(id=res[0].id).update(user_password=nw)
            return HttpResponse("<script>alert('password changed...');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('password Missmatch...');window.location='/change_password'</script>")

    return HttpResponse("<script>alert('password not found...');window.location='/change_password'</script>")

def payment_method(request,id,amnt):
    request.session['amnt'] = amnt
    return render(request,"client/method.html",{"id":id})

def payment_method_post(request,id):
    request.session['oid'] = id
    if request.POST['radio'] == 'Offline':
        order.objects.filter(id=request.session['oid']).update(status='Offline', total_price=request.session['amnt'])
        data2 = order_sub.objects.filter(ORDER_id=request.session['oid'])
        for ij in data2:
            if int(ij.quantity) > int(ij.STOCK.stock):
                ij.delete()
            else:
                xx = int(ij.STOCK.stock) - int(ij.quantity)
                stock.objects.filter(id=ij.STOCK.id).update(stock=xx)
        data2 = order_sub.objects.filter(ORDER_id=id)
        for ij in data2:
            if int(ij.quantity) > int(ij.STOCK.stock):
                pass
            else:
                 xx = int(ij.STOCK.stock) - int(ij.quantity)
                 stock.objects.filter(id = ij.STOCK.id).update(stock = xx)
        return HttpResponse("<script>alert('Ordered succesfull..');window.location='/view_request_status#contents'</script>")
    else:
        import razorpay

        razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
        razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

        razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

        amount = int(request.session['amnt']) * 100
        # amount = float(amount)

        # Create a Razorpay order (you need to implement this based on your logic)
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': '1',  # Auto-capture payment
        }

        # Create an order
        orders = razorpay_client.order.create(data=order_data)

        context = {
            'razorpay_api_key': razorpay_api_key,
            'amount': order_data['amount'],
            'currency': order_data['currency'],
            'order_id': orders['id'],
        }
        return render(request,"client/payment.html",{'razorpay_api_key': razorpay_api_key,'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            'order_id': orders['id']})


def payment_entry(request):
    obj = payment()
    obj.ORDER_id = request.session['oid']
    obj.ammount = request.session['amnt']
    obj.payment_date = datetime.datetime.now()
    obj.USER_id = request.session['cid']
    obj.save()
    order.objects.filter(id=request.session['oid']).update(status='Online',total_price = request.session['amnt'])
    data2 = order_sub.objects.filter(ORDER_id=request.session['oid'])
    for ij in data2:
        if int(ij.quantity) > int(ij.STOCK.stock):
            ij.delete()
        else:
            xx = int(ij.STOCK.stock) - int(ij.quantity)
            stock.objects.filter(id=ij.STOCK.id).update(stock=xx)
    return redirect('/view_request_status')

def logout(request):
    request.session['lg']=""
    return HttpResponse("<script>alert('Log out successfully');window.location='/'</script>")

def forget(request):
    return render(request,"forget.html")
def forget_post(request):

    forgetpas = request.POST['forgetpass']
    x = login.objects.filter(user_name=forgetpas)
    if x.exists():
        try:
            import smtplib
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(memail, mpass)
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = memail
            msg['To'] = x[0].user_name
            msg['Subject'] = "Your MaterialHub password"
            body = "Your password is " + str(x[0].user_password)
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)

        except:
            pass

        return HttpResponse("<script>alert('password was sented your email..');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Email is invalid...');window.location='/forget'</script>")