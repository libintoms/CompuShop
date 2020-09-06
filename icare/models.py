from django.db import models

# Create your models here.
class Products(models.Model):
    prod_name=models.CharField(max_length=100)
    prod_price=models.IntegerField()
    image=models.ImageField(upload_to='media/images')
    home_display=models.BooleanField(default=False)
    offer_price=models.IntegerField()

    def __str__(self):
        return self.prod_name
    class Meta:
        verbose_name_plural = "Product list"

