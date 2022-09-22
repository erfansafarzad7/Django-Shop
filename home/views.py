from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Products, Category
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin
from orders.forms import CartAddForm


class HomeView(View):
    def get(self, request, category_slug=None):
        products = Products.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        form = CartAddForm()
        return render(request, 'home/detail.html', {'product': product, 'form': form})


class BucketHomeView(IsAdminUserMixin, View):
    temp_name = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.temp_name, {'objects': objects})


class DeleteBucketView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_obj_task(key)
        # tasks.delete_obj_task.delay(key)
        messages.success(request, 'Your Object Will Be Delete Soon', 'info')
        return redirect('home:bucket')


class DownloadBucketView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task(key)
        # tasks.download_object_task.delay(key)
        messages.success(request, 'Your Object Will Be Download Soon', 'info')
        return redirect('home:bucket')

