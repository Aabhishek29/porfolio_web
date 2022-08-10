from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def contactme(request):
    return render(request,'contactme.html')

def projects(request):
    return render(request,'projects.html')
