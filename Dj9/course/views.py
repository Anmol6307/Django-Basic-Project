from django.shortcuts import render

# Create your views here.

def Learn_Django(request):
    return render(request, 'course/course1.html', {'title':'learndjango', 'cname':'Django'})
