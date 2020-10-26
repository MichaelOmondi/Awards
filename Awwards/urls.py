from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path, include
from . import views
from .views import home, project_view, signup, profile, edit_profile, upload, index

# Creating the urls

urlpatterns = [
    path('', home, name='home'),
    path('project/<post>',views.project_view, name='project'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload, name='upload'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)