# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Student Management System!")
## change for template
from django.shortcuts import render

def home(request):
    return render(request, "students/home.html")


