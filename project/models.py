from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from PIL import Image

# Create your models here.
class Project(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project/')
    title=models.CharField(max_length=60)
    description=models.TextField()
    link=models.CharField(max_length=100)
    location=models.CharField(max_length=30)
    posted=models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        super().save()
        img=Image.open(self.image.path)
        
        if img.height>720 and img.width>720:
            size=(720,720)
            img.thumbnail(size)
            img.save(self.image.path)
        
    def __str__(self):
        return self.title
    
    def save_project(self):
        self.save()
    
    @classmethod    
    def get_project(cls, id):
        project=Project.objects.get(pk=id)
        return project
    
    @classmethod   
    def delete_project(cls,delete_id):
        Project.objects.filter(pk=delete_id).delete()
        
        
class Votes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    usability=models.IntegerField(default=0, validators=[MaxValueValidator(10,message='Range acceptable is 0-10'), MinValueValidator(0)])
    design=models.IntegerField(default=0, validators=[MaxValueValidator(10,message='Range acceptable is 0-10'), MinValueValidator(0)])
    content=models.IntegerField(default=0, validators=[MaxValueValidator(10,message='Range acceptable is 0-10'), MinValueValidator(0)])
    
    def __str__(self):
        return self.user.username
    
    
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/', default='default.png')
    bio=models.TextField(blank=True)
    contact=models.CharField(max_length=30, blank=True)
    location=models.CharField(max_length=50,  blank=True)
    company=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        super().save()
        
        img=Image.open(self.image.path)
        
        if img.height>400 and img.width>400:
            size=(400,400)
            img.thumbnail(size)
            img.save(self.image.path)
            
