from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login')
def home(request):

    return render(request, 'home.html')


@login_required(login_url='/account/login')
def post(request):
    
    return render(request, 'post.html')