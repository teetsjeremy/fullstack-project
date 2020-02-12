from django.db import models

# Create your models here.
class Patterns(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)
    
    
    def __unicode__(self):
        return self.description
    