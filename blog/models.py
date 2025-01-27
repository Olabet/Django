from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text=models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = models.DateTimeField(default=timezone.now)
        self.save()
    
    def __str__(self) :
        return self.title
    