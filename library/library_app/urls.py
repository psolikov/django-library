from django.urls import path

from . import views

app_name = 'library_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('available-books/', views.view_all_available_books, name='available-books'),
    path('students-books/', views.students_books, name='students-books'),
    path('<int:student_id>/student-books/', views.student_books, name='student-books'),
    path('student-operation/', views.student_operation, name='student-operation'),
    path('make-operation/', views.make_operation, name='make-operation'),
]
