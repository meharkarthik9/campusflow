from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.decorators import login_required


@login_required
def student_list(request):

    query = request.GET.get('search')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            course=course
        )

        return redirect('/students/')

    return render(request, 'students/add.html')

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students/')

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('/students/')

    return render(request, 'students/edit.html', {'student': student})

