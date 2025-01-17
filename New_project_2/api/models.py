from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
