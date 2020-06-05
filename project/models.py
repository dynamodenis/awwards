from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project/', blank=True)
    title=models.CharField(max_length=60)
    description=models.TextField()
    posted=models.DateTimeField(auto_now_add=True) 
    usability=models.ManyToManyField(User, related_name='usability', blank=True)
    design=models.ManyToManyField(User, related_name='design' , blank=True)
    content=models.ManyToManyField(User, related_name='content' , blank=True)
    
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
        
