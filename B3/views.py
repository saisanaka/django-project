from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import Destination

def index(requset):
	dest = Destination()
	dest.title = "maldives"
	dest.img = "maldives/2918339.jpg"
	dest.price = 572

	dest1 = Destination()
	dest1.title = "kenya"
	dest1.img = "maldives/2918305.jpg"
	dest1.price = 372

	dest2 = Destination()
	dest2.title = "machu pichu"
	dest2.img = "maldives/902479.jpg"
	dest2.price = 382

	dests = [dest , dest1 , dest2 ]
	return render(requset,'index.html' , {"dests":dests})

def signup(r):
	return render(req,'payment.html')

def logout(r):
	auth.logout(r)
	return redirect('/')


def log(req):
	username = req.POST['username']
	mail = req.POST['password']
	user = auth.authenticate(username=username,password=mail)
	if user is not None:
		auth.login(req,user)
		return redirect('/')
	else:
		messages.info(req , "invalid credentials")
		return render(req , "login.html")

def register(req):
	username = req.POST['username']
	mail = req.POST['email']
	p1 = req.POST['password']
	p2 = req.POST['pass']
	if p1 == p2 :
		if User.objects.filter(username=username).exists():
			return render(req , "sign-err.html")

		elif User.objects.filter(email=mail).exists():
			return render(req , "sign-err3.html")

		else:
			user = User.objects.create_user(username=username , password = p1, email = mail)
			user.save()
			return render(req,'login.html')
	else:
		
		return render(req , "sign-err2.html")

def payment(req):
	return render(req,'payment.html')

def success(req):
	return render(req,'success.html')

def hotel(req):
	return render(req,'hotel.html')

def signup(req):
	return render(req,'signup.html')

def login(req):
	return render(req,'login.html')