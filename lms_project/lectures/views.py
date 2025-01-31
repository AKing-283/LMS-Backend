from django.shortcuts import render, redirect
from .models import Lecture
from .forms import LectureForm

def upload_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_lectures')
    else:
        form = LectureForm()
    return render(request, 'lectures/upload_lecture.html', {'form': form})

def view_lectures(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures/view_lectures.html', {'lectures': lectures})