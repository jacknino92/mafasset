from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
	#path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    #path('asset/', views.login1, name='asset')
    path('index/', views.index, name='index'),
    


]
