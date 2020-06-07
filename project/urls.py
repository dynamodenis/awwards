from django.urls import path,include
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import ProjectList


# router=routers.DefaultRouter()
# router.register('project',views.ProjectList)

app_name='project'
urlpatterns = [
    path('', views.index,name='project_index'),
    path('user/profile/', views.profile,name='profile'),
    path('project/<int:project_id>/', views.project,name='project'),
    path('new/project/', views.new_project,name='new_project'),
    path('user/<int:user_id>', views.posted_by,name='posted_by'),
    #API PATTERN
    path('api/project/', views.ProjectList.as_view()),
    path('api/users/', views.UserList.as_view()),
    path('api/project/<int:pk>/',views.ProjectDescription.as_view()),
    path('api/user/<int:pk>/',views.UserDescription.as_view()),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
