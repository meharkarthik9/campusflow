from django.urls import path
from .views import student_list, add_student, delete_student, edit_student
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', student_list),
    path('students/', student_list),
    path('add/', add_student),
    path('delete/<int:id>/', delete_student),
    path('edit/<int:id>/', edit_student),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]