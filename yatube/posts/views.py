from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<p>Hello, World!</p>')


def group_posts(request, num):
    return HttpResponse(f'This is {num}')
