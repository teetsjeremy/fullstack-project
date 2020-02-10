from django.db import models
from django.utils import timezone

# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True,Null=False, default=timezone.now)
    
    def __unicode__(self):
        return self.first_name