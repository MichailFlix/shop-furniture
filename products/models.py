from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    def get_image(self):
        return self.image.url

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    # Добавить Seller или Brand

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()

    def get_image(self):
        return self.image.url

    def __str__(self):
        return self.name