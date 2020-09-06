from django.shortcuts import render
from . models import Products

# Create your views here.
def index(request):
    productn=Products.objects.all()

    return render(request,"index.html",{'productn':productn})

def about(request):
    return render(request,"it_about.html")