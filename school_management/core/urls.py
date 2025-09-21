from django.urls import path
from . import views

urlpatterns = [
    # Students
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Teachers
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:id>/', views.teacher_update, name='teacher_update'),
    path('teachers/delete/<int:id>/', views.teacher_delete, name='teacher_delete'),
]
