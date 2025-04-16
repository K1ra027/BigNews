from django.shortcuts import render,get_object_or_404,redirect
from .models import News, Category
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm, LoginForm



# Create your views here.




def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news':news,
        'categories':categories
    }
    return render(request, 'home.html', context)

def detail(request, id):
    new = get_object_or_404(News, id=id)
    context = {
        'new':new,
    }
    return render(request, 'detail.html',context)
def category(request, id):
    category = News.objects.filter(category_id=id)
    categories = Category.objects.all()
    context = {
        'category':category,
        'categories':categories,
    }
    return render(request, 'category.html', context)


def registration(request):
    if request.method == 'POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('home')


def log_in(request):
    if request.method =='POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form':form})


