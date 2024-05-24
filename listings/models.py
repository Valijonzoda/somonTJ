from django.db import models
from core.models import Categories, Locations
class Listing(models.Model):
    listings_id = models.AutoField("listings_id", primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/listings/')
    price = models.FloatField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Listings'
