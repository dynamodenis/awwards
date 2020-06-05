from django.shortcuts import render,redirect
from .forms import RegisterUser
from .email import send_welcome_email
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            send_welcome_email(username,email)
            
            messages.success(request,f'Account created successfully, you can login!')
            return redirect('login')
        
    else:
        form=RegisterUser()
        
    return render(request,'registration/register.html',{'form':form})
