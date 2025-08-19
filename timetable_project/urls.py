from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),   # Default page = Register
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('classes/', views.class_list, name='class_list'),
    path('add_class/', views.add_class, name='add_class'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_period/', views.add_period, name='add_period'),
    path('class/<int:class_id>/timetable/', views.view_timetable, name='view_timetable'),
]
