from django.core.checks import messages
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import ImagePost, category, Location
# Create your views here.

def index(request):
  '''
  Function that displays the homepage of the app
  '''
  posts = ImagePost.all_images()
  locations = Location.objects.all()
  return render(request, 'index.html', {"posts" : posts , 'locations': locations})

def search_results(request):
  if 'category' in request.GET and request.GET["category"]:
    search_term = request.GET.get('category')
    try:
      cat_name = category.objects.get(cat_name = search_term)
      cat_id = cat_name.id
      searched_categories = ImagePost.search_category(cat_id)
      message = f"{search_term}"
    except ObjectDoesNotExist:
      raise Http404()
    return render(request, 'search.html', {"message": message, "categories":searched_categories })
  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message": message})

def find_by_location(request):
  '''
  Function to find image posts based on their location
  '''
  
  images = ImagePost.filter_by_location()
  return render(request , 'location.html', {'images':images})