from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from .forms import PostProject,UpdateUser,UpdateProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    projects=Project.objects.order_by('-posted')
    return render(request,'project/index.html',{'projects':projects})

#user profile
@login_required
def profile(request):
    return render(request,'project/profile.html')


#specific project
def project(request,project_id):
    project=get_object_or_404(Project,pk=project_id)
    return render(request, 'project/project.html',{'project':project})

def new_project(request):
    current_user=request.user
    if request.method=='POST':
        form=PostProject(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=current_user
            project.save()
        return redirect('project:project_index')
    
    else:
        form=PostProject()
        
    return render(request,'project/new_project.html',{'form':form})

def posted_by(request, user_id):
    user=get_object_or_404(User,pk=user_id)
    return render(request,'project/posted_by.html', {'user':user})
            