from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Book, Student

def index(request):
    context = {}
    template = loader.get_template('library_app/index.html')
    return HttpResponse(template.render(context, request))

def view_all_available_books(request):
    books = Book.objects.all().filter(current_student__isnull=True)
    res = ''
    for b in books:
        res += str(b) + ';'
    return HttpResponse(f"Available books in library: {res}")

def student_operation(request):
    context = {}
    template = loader.get_template('library_app/take_or_return_book.html')
    return HttpResponse(template.render(context, request))

def make_operation(request):
    student_id = request.POST['student']
    book_id = request.POST['book']
    operation = request.POST['operation']
    book = get_object_or_404(Book, pk=book_id)
    student = get_object_or_404(Student, pk=student_id)
    if operation == 'take':
        if book.current_student:
            return HttpResponse(f'Book {book_id} is taken by other student')
        book.current_student = student
        book.save()
        return HttpResponse('Done')
    elif operation == 'return':
        if not book.current_student:
            return HttpResponse(f'Book {book_id} is free')
        if book.current_student != student:
            return HttpResponse(f'Book {book_id} is taken by other student')
        book.current_student = None
        book.save()
        return HttpResponse('Done')
    else:
        return HttpResponse(f'Wrong operation: {operation}')

def students_books(request):
    students = Student.objects.all()
    context = {'students_list': students}
    template = loader.get_template('library_app/student_books.html')
    return HttpResponse(template.render(context, request))

def student_books(request, student_id):
    taken_books = []
    books = Book.objects.all()
    student = get_object_or_404(Student, pk=student_id)
    for b in books.all():
        if b.current_student == student:
            taken_books.append(b)
    res = ''.join(str(e) + '<br>' for e in taken_books)
    return HttpResponse(f'Taken books for student {student_id}: {res}')
