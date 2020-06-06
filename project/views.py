from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'project/index.html')

#user profile
@login_required
def profile(request):
    return render(request,'project/profile.html')
    