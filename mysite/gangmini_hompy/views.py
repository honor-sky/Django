from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("GANGMINI_HOMPY")
'''
def index(request):
    return render(request,'gangmini_hompy/index.html')
