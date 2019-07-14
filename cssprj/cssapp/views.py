from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def mediaq(request):
    return render(request, 'mediaq.html')