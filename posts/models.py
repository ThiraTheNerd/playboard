from django.db import models

# Create your models here.
class Location(models.Model):
  loc_name = models.CharField(max_length=50)
  def __str__(self):
    return self.loc_name
  def save_location(self):
    '''
    Save Location instance
    '''
    self.save()
  
  def delete_location(self):
    '''
    Remove the instance of a location
    '''
    self.delete()
  
  def update_location(self):
    '''
    Update the model columns
    '''
    self.save()

class category(models.Model):
  cat_name = models.CharField(max_length=30)
  def __str__(self):
    return self.cat_name

  def save_category(self):
    '''
    Save category instance
    '''
    self.save()
  
  def delete_category(self):
    '''
    Remove the instance of a category
    '''
    self.delete()
  
  def update_category(self):
    '''
    Update the model columns
    '''
    self.save()
  


class ImagePost(models.Model):
  image = models.ImageField(upload_to = 'posts/')
  image_name = models.CharField(max_length=50)
  image_description = models.CharField(max_length=200)
  post_date= models.DateTimeField(auto_now_add = True)
  location = models.ForeignKey(Location , on_delete = models.CASCADE, null=True)
  category = models.ForeignKey(category , on_delete = models.CASCADE, null=True)

  def __str__(self):
    return self.image_name

  def save_imagepost(self):
    '''
    Save Image Post instance
    '''
    self.save()
  
  def delete_imagepost(self):
    '''
    Remove the instance of an imagepost
    '''
    self.delete()
  
  def update_imagepost(self):
    '''
    Update the model columns
    '''
    self.save()

  @classmethod
  def all_images(cls):
    all_images = cls.objects.all()
    return all_images

  
  @classmethod
  def get_image_by_id(cls,image_id):
    '''
    Function for acessing a single image post
    '''
    images=cls.objects.get(pk = image_id)
    return images

  @classmethod 
  def search_category(cls, id):
    '''
    Function to search for an image post
    '''
    images = cls.objects.filter(category=id)
    return images

  @classmethod 
  def filter_by_location(cls):
    '''
    Function to filter based on the imagepost location
    '''
    images = cls.objects.all()
    return images
    