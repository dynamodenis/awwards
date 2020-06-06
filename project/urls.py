from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static

app_name='project'
urlpatterns = [
    path('', views.index,name='project_index'),
    path('user/profile/', views.profile,name='profile'),
    path('project/<int:project_id>/', views.project,name='project'),
    path('new/project/', views.new_project,name='new_project'),
    path('user/<int:user_id>', views.posted_by,name='posted_by'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
