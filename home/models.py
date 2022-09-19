from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    sluge = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name