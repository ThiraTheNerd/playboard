from django.shortcuts import render
from .models import ImagePost, category, Location
# Create your views here.

def index(request):
  '''
  Function that displays the homepage of the app
  '''
  posts = ImagePost.all_images()
  
  return render(request, 'index.html', {"posts" : posts})