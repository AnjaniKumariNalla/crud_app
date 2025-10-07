from django.db import models

class Movies(models.Model):
    STATUS_CHOICES = [
      
        ('Completed', 'Completed'),
        ('Plan to Watch', 'Plan to Watch'),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1) 
    # image_url = models.URLField(max_length=500, blank=True) 
    image_url = models.ImageField(upload_to='movies/', blank=True, null=True)


    def __str__(self):
        return self.title