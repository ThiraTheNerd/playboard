from django.shortcuts import render

# Create your views here.

def index(request):
  '''
  Function that displays the homepage of the app
  '''
  return render(request, 'index.html')