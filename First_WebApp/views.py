
from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
	return render(request,'index.html',{'key1':'I am coming from Python code'})

def result(request):
	# name = request.GET.get('user_name')
	# age=request.GET.get('user_age')
	# message = f'Hi {name}, you are {age} years old '

	article = request.GET.get('article')
	sorted_dict_word,word_count = counter.count(article)
	return render(request,'result.html',{'art':article,'word_count':word_count,'dict_word':sorted_dict_word})





# def downloads(request):
# 	return HttpResponse('<h1>No Downloads Here</h1>')