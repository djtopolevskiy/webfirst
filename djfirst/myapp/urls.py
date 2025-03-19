app_name = 'myapp'
from django.urls import path
from myapp import views

urlpatterns = [  
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('', views.index, name='home'),
	path('<int:my_id>/', views.indexItem, name='homeItem'),
]
