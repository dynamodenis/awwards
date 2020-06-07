from rest_framework import serializers
from .models import Project

#project serailizers
class ProjectSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id','title','description','link','posted']