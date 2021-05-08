from django.shortcuts import render

# Create your views here.
def home_function(request):
    return render(request,'home.html')