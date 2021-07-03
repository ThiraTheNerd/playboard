from django.test import TestCase
from .models import category,Location,ImagePost

# Create your tests here.

class CategoryTest(TestCase):
  def setUp(self):
    '''
    Creates an instance of the category model
    '''
    self.category = category(cat_name ='fashion')
  
  def test_instance(self):
    '''
    Test the instation of the category model
    '''
    self.assertTrue(isinstance(self.category,category))

class LocationTest(TestCase):
  def setUp(self):
    '''
    Creates an instance of the category model
    '''
    self.location = Location(loc_name ='Ukraine')
  def test_instance(self):
    '''
    Test the instatioation of location model
    '''
    self.assertTrue(isinstance(self.location,Location))

class CategoryTest(TestCase):
  def setUp(self):
    '''
    Creates an instance of the ImagePost model
    '''
    self.imagepost = ImagePost(image ='mango.jpeg', image_name='Mountains', 
    image_description= 'This is beautiful')
  
  def test_instance(self):
    '''
    Test the instation of the ImagePost model
    '''
    self.assertTrue(isinstance(self.imagepost,ImagePost))
  
  def test_save_imagepost(self):
    '''
    Test save imagepost method
    '''
    self.imagepost.save_imagepost()
    posts = ImagePost.objects.all()
    self.assertTrue(len(posts) > 0)

