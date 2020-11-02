from django.shortcuts import render,redirect
from .models import Signup,Oneplus,Iphone,Samsung,Order,Tshirt,Shirt,Shoe,Watch,Jeans,Hp,Dell,Lenovo
from .forms import SignupForm,OrderForm, ContactForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import settings  
from django.core.mail import send_mail 
import random


def master(request):
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		return render(request, 'master.html', {'rs':rs})
	except KeyError:
		return render(request, 'master.html')
	else:
		return render(request, 'master.html')

def mail(request):
	otp = random.randint(100000, 999999)
	subject = "Reset Password Request."
	msg = "Your new password is - " + str(otp)
	to = request.POST["e1"]
	rs = Signup.objects.filter(email=to).update(password = otp)
	if rs:
		res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
		if(res == 1):
			msg = "Mail Sent Successfuly, Please check your mail and login again!"
		else:
			msg = "Mail could not sent"
		return HttpResponse(msg)
	else:
		return HttpResponse("You have entered wrong email!!!")


def login(request):
	try:
		if request.method=="POST" and "login" in request.POST:
			uem = request.POST["email"]
			pas = request.POST["password"]
			show="Invalid user"
			request.session['usremail']=uem
			checkusr = Signup.objects.filter(email=uem, password=pas)
			if checkusr:
				rs = Signup.objects.get(email=uem)
				return render(request,'master.html', {'rs':rs})
			else:
				return render(request,'master.html',{'show':show})
		elif request.method=="POST" and "signup" in request.POST:
			form = SignupForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse("Registered...")
			else:
				return HttpResponse("Error!, Not registered")
		elif request.method=="POST" and "contact" in request.POST:
			form = ContactForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse("Message sent successfully...")
			else:
				return HttpResponse("Error!, Something went wrong...<br> Please try again!")
		elif request.method=="POST" and "forget" in request.POST:
			otp = random.randint(100000, 999999)
			subject = "Reset Password Request."
			msg = "Your new password is - " + str(otp)
			to = request.POST["email"]
			rs = Signup.objects.filter(email=to).update(password = otp)
			if rs:
				res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
				if(res == 1):
					msg = "Mail Sent Successfuly, Please check your mail and login again!"
				else:
					msg = "Mail could not sent"
				return HttpResponse(msg)
			else:
				return HttpResponse("You have entered wrong email!!!")
		elif request.method=="POST" and "update" in request.POST:
			session = request.session["usremail"]
			rs=Signup.objects.get(email=session)
			form=SignupForm(request.POST, instance=rs)
			if form.is_valid():
				form.save()
				return redirect('../profile/')
			else:
				return HttpResponse("Unable to update")
		else:
			return render(request,'master.html')
	except KeyError:
		return render(request, 'master.html')

def profile(request):
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		return render(request, 'profile.html', {'rs':rs})
	except:
		return render(request, 'master.html')
	else:
		return render(request, 'master.html')


def edit(request,id):
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(id=id, email=session)
		return render(request,'edit.html',{'rs':rs})
	except:
		return HttpResponse("<h1 align='center'>~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 404 - Not Found ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ </h1>")

def update(request,id):
	if request.method=="POST" and "update" in request.POST:
		session = request.session["usremail"]
		rs=Signup.objects.get(id=id, email=session)
		form=SignupForm(request.POST, instance=rs)
		if form.is_valid():
			form.save()
			return redirect('../profile/')
		else:
			return HttpResponse("Unable to update")
	else:
		return HttpResponse("Error")

def mobile(request):
	products = Oneplus.objects.all()
	iphone = Iphone.objects.all()
	samsung = Samsung.objects.all()
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		if products and iphone and samsung and rs:
			return render(request, 'mobile.html', {'products':products, 'iphone':iphone, 'samsung':samsung, 'rs':rs})
	except:
		return render(request, 'mobile.html', {'products':products, 'iphone':iphone, 'samsung':samsung })
	else:
		return HttpResponse("Error")

def laptop(request):
	hp = Hp.objects.all()
	dell = Dell.objects.all()
	lenovo = Lenovo.objects.all()
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		if hp and dell and lenovo and rs:
			return render(request, 'laptop.html', {'hp':hp, 'dell':dell, 'lenovo':lenovo, 'rs':rs})
	except:
		return render(request, 'laptop.html', {'dell':dell, 'hp':hp, 'lenovo':lenovo })
	else:
		return HttpResponse("Error")

def pdetail(request,id):
    ors = Oneplus.objects.get(id=id)
    try:
    	session = request.session["usremail"]
    	rs = Signup.objects.get(email=session)
    	return render(request, 'pdetail.html', {'records':ors, 'rs':rs})
    except:
        return render(request, 'pdetail.html', {'records':ors})
    else:
        return render(request, 'pdetail.html', {'records':ors})
def idetail(request,id):
    irs = Iphone.objects.get(id=id)
    try:
    	session = request.session["usremail"]
    	rs = Signup.objects.get(email=session)
    	return render(request, 'idetail.html', {'records':irs, 'rs':rs})
    except:
        return render(request, 'idetail.html', {'records':irs})
    else:
        return render(request, 'idetail.html', {'records':irs})
def sdetail(request,id):
	srs = Samsung.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'sdetail.html', {'records':srs, 'rs':rs})
	except:
	    return render(request, 'sdetail.html', {'records':srs})
	else:
	    return render(request, 'sdetail.html', {'records':srs})
def shoedetail(request,id):
	shoers = Shoe.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'shoedetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'shoedetail.html', {'records':shoers})
	else:
	    return render(request, 'shoedetail.html', {'records':shoers})
def wdetail(request,id):
	shoers = Watch.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'wdetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'wdetail.html', {'records':shoers})
	else:
	    return render(request, 'wdetail.html', {'records':shoers})
def shdetail(request,id):
	shoers = Shirt.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'shdetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'shdetail.html', {'records':shoers})
	else:
	    return render(request, 'shdetail.html', {'records':shoers})
def jdetail(request,id):
	shoers = Jeans.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'jdetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'jdetail.html', {'records':shoers})
	else:
	    return render(request, 'jdetail.html', {'records':shoers})
def delldetail(request,id):
	dellrs = Dell.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'delldetail.html', {'records':dellrs, 'rs':rs})
	except:
	    return render(request, 'delldetail.html', {'records':dellrs})
	else:
	    return render(request, 'delldetail.html', {'records':dellrs})
def hpdetail(request,id):
	shoers = Hp.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'hpdetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'hpdetail.html', {'records':shoers})
	else:
	    return render(request, 'hpdetail.html', {'records':shoers})
def ldetail(request,id):
	shoers = Lenovo.objects.get(id=id)
	try:
	    session = request.session["usremail"]
	    rs = Signup.objects.get(email=session)
	    return render(request, 'ldetail.html', {'records':shoers, 'rs':rs})
	except:
	    return render(request, 'ldetail.html', {'records':shoers})
	else:
	    return render(request, 'ldetail.html', {'records':shoers})


def mens(request):
	shoe = Shoe.objects.all()
	watch = Watch.objects.all()
	jeans = Jeans.objects.all()
	shirt = Shirt.objects.all()
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		return render(request, 'mens.html', {'shoe':shoe,'watch':watch, 'jeans':jeans, 'shirt':shirt, 'rs':rs})
	except:
		return render(request, 'mens.html', {'shoe':shoe,'watch':watch, 'jeans':jeans, 'shirt':shirt})

def logout(request):
	try:
		del request.session["usremail"]
	except KeyError:
		pass
	return redirect("../")

def delete(request,id):
    Signup.objects.get(id=id).delete()
    return HttpResponse("Account has been deleted..")

def about(request):
	return render(request, 'about.html')
def contact(request):
	if request.method=="POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Message sent successfully...")
		else:
			return HttpResponse("Error!, Something went wrong...<br> Please try again!")
	try:
		session = request.session["usremail"]
		rs = Signup.objects.get(email=session)
		return render(request, 'contact.html', {'rs':rs})
	except:
		return render(request, 'contact.html')
	else:
		return render(request, 'contact.html')

def forget(request):
	return render(request, 'forget.html')