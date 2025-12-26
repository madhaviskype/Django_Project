from django.shortcuts import render, redirect,get_object_or_404
from .models import Teacher

# 1️⃣ DISPLAY DATA
def teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'index.html', {'teacher_list': teacher_list})


# 2️⃣ ADD DATA
def add_teacher(request):
    if request.method == "POST":
        print(request.POST)
        Teacher.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            location=request.POST.get('location'),
        )
    return redirect('teachersdata')
def update_teacher(request, id):
    # Fetch the existing teacher
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        # Update fields using request.POST
        teacher.name = request.POST.get('name')
        teacher.email = request.POST.get('email')
        teacher.subject = request.POST.get('subject')
        teacher.location = request.POST.get('location')
        teacher.save()  # Save changes to database
        return redirect('teachersdata')

    # Render a template if needed (optional)
    return render(request, 'index.html', {'teacher': teacher})

def delete_teacher(request,id):
    teacher=Teacher.objects.filter(id=id)
    teacher.delete()
    return redirect('teachersdata')