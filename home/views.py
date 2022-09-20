from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Products
from . import tasks
from django.contrib import messages

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
        objects = tasks.all_bucket_objects_task()
        return render(request, self.temp_name, {'objects': objects})


class DeleteBucketView(View):
    def get(self, request, key):
        tasks.delete_obj_task(key)
        messages.success(request, 'Your Object Will Be Delete Soon', 'info')
        return redirect('home:bucket')

