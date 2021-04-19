from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

#added all of these content:
def index(request):
    return HttpResponse('yaaay....ya welcome')

def home(request):
    return HttpResponse('hello king...')


