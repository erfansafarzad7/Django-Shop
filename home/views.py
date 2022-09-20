from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Products
from .tasks import all_bucket_objects_task


class HomeView(View):
    def get(self, request):
        products = Products.objects.filter(available=True)
        return render(request, 'home/index.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        return render(request, 'home/detail.html', {'product': product})


class BucketHoneView(View):
    temp_name = 'home/bucket.html'

    def get(self, request):
        objects = all_bucket_objects_task()
        return render(request, self.temp_name, {'objects': objects})
