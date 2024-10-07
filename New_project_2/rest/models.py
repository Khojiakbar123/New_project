from django.db import models

# Create your models here.
class CategoryRest(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CarRest(models.Model):
    title = models.CharField(max_length=150)
    model = models.CharField(max_length=50)
    manufactured = models.IntegerField(default=1999)
    color = models.CharField(max_length=40, default="Black", verbose_name="Car Color")
    max_speed = models.IntegerField(default=100)
    horsepower = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("CategoryRest", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

