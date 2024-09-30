from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Home (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def About (request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def Contact (request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def Faq (request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())


#影片欄位，圖片更新
