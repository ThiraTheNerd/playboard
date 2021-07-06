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
  def test_save_category(self):
    '''
    Test save category method
    '''
    self.category.save_category()
    categories = category.objects.all()
    self.assertTrue(len(categories) > 0)
  def test_delete_category(self):
    '''
    Test the deletion of an instance
    '''
    self.category.save_category()
    self.category.delete_category()
    categories = category.objects.all()
    self.assertTrue(len(categories) == 0)

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
  def test_save_category(self):
    '''
    Test save category method
    '''
    self.location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) > 0)
  
  def test_delete_location(self):
    '''
    Test the deletion of an instance
    '''
    self.location.save_location()
    self.location.delete_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) == 0)

class ImagePostTest(TestCase):
  def setUp(self):
    '''
    Creates an instance of the ImagePost model
    '''
    self.imagepost = ImagePost(id = 1, image ='mango.jpeg', image_name='Mountains', 
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

  def test_all_images(self):
    self.imagepost.save_imagepost()
    all_posts = ImagePost.all_images()
    print(all_posts)
    self.assertTrue(len(all_posts) == 1)

  def test_delete_imagepost(self):
    '''
    Test the deletion of an instance
    '''
    self.imagepost.save_imagepost()
    self.imagepost.delete_imagepost()
    posts = ImagePost.objects.all()
    self.assertTrue(len(posts) == 0)

  # def test_update_imagepost(self):
  #   '''
  #   Test the update imagepost method
  #   '''
  #   self.imagepost.save_imagepost()
  #   images = ImagePost.objects.filter(id = 2).update(image_name = 'Valley')
  #   print(images)
  #   images.update_imagepost()
  #   self.assertEqual(self.imagepost.image_name, 'Valley')

  def test_get_image_by_id(self):
    self.imagepost.save_imagepost()
    image_id= self.imagepost.pk
    image_by_id = ImagePost.get_image_by_id(image_id)
    self.assertEqual(self.imagepost,image_by_id)

  def test_search_category(self):
    self.imagepost.save_imagepost()
    id = self.imagepost.id
    found_image = ImagePost.search_category(id)
    print(found_image)
    self.assertTrue(len(found_image) > 1)
  
  # def test_filter_by_location(self):
  #   self.imagepost.save_imagepost()
  #   location = self.imagepost.location
  #   found_images = ImagePost.filter_by_location(location)
  #   self.assertEqual(self.imagepost,found_images)
  def tearDown(self):
    ImagePost.objects.all().delete()
    

