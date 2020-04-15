from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import projecttable
def index(request):
	return render(request,'index.html')
def signup(request):
	if request.method=='POST':


		x=request.POST.get('name')
		y=request.POST.get('email')
		z=request.POST.get('pass')
		a=projecttable(username=x,email=y,password=z)
		a.save()
		return redirect('n3')
	else:
		return render(request,'signup.html')
def login(request):
	if request.method=='POST':
		x=request.POST['your_name']
		y=request.POST['your_pass']
		try:
			d1=projecttable.objects.get(username=x,password=y)
		except projecttable.DoesNotExist:
			return render(request,'login.html')
		else:
			request.session['username']=d1.username
			return redirect('n1')
	else:
		return render(request,'login.html')
def signout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return render(request,'login.html')