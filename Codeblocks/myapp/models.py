from django.db import models

# Create your models here.


class Domain(models.Model):
    d_name = models.CharField(max_length=200)
    d_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.d_name
    
class Events(models.Model):
    e_name = models.CharField(max_length=200)
    e_desc = models.TextField(null=True, blank=True)
    e_image = models.ImageField(null=True,blank=True,default='default.jpg')

    def __str__(self):
        return self.e_name
    
    def imageURL(self):
        
        try:
            img = self.e_image.url
        except:
            img = 'static/images/default.jpg'
        return img
    
  
