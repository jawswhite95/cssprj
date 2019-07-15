from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def mediaq(request):
    return render(request, 'mediaq.html')
def sex(request):
    return render(request, 'sex.html')
def news(request):
    return render(request, 'news.html')
def sanitary(request):
    return render(request, 'sanitary.html')
def detail(request):
    return render(request, 'detail.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
    