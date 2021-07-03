from django.db import models

# Create your models here.
class Location(models.Model):
  loc_name = models.CharField(max_length=50)

class category(models.Model):
  cat_name = models.CharField(max_length=30)

class ImagePost(models.Model):
  image = models.ImageField(upload_to = 'posts/')
  image_name = models.CharField(max_length=50)
  image_description = models.CharField(max_length=200)
  post_date= models.DateTimeField(auto_now_add = True)
  location = models.ForeignKey(Location , on_delete = models.CASCADE, null=True)
  category = models.ManyToManyField(category)

  def __str__(self):
    return self.image_name

  def save_imagepost(self):
    self.save()


  

  