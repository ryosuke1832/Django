from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    image = models.ImageField(null=True, upload_to='media/images')
    posted_at = models.DateField()
    updated_at = models.DateField()
    
    def __str__(self):
        return self.title
