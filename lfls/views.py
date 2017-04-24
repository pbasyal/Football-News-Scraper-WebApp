from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .forms import RegisterForm
from .models import User
from . import webscrapping

news_ = webscrapping.run()
# print(news_)

# Create your views here.
def main_view(request):
	# print(news_)
	return render(request,'news.html', {'page_title': 'LFNews - SportingCP', 'news':news_})

def register(request):
	if request.method == 'GET':
		form = RegisterForm()
		return render(request, 'register.html', {'form':form})
	elif request.method == 'POST':
		if form.is_valid():
			username_ = form.cleaned_data['username']
			password_ = form.cleaned_data['password']
			email_ = form.cleaned_data['email']
			u1 = User(username=username_, password=password_, email=email_)
			u1.save()
			return HttpResponse('User successfully registered!')
		else:
			return HttpResponse('Form is not valid')

def news_id(request, id):
	global news_
	for elm in news_:
		if(int(elm['id']) == int(id)):
			item = webscrapping.get_news_full_text(elm['link'])
			return render(request, 'news_detail.html', {'item': item , 'page_title':'LFNews: %s' % item['header']['title'] })
	
	return HttpResponse("News id is invalid")	

def about(request):
	return render(request,'about.html', {'page_title': 'About me'})