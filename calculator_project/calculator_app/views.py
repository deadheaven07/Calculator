from django.shortcuts import render

# Create your views here.
# calculator_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'calculator_app/index.html')

