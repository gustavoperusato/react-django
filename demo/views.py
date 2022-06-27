from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1> Hey Crabber! </h1>
    <h2>Currently, this system is under production.</h2>''')


