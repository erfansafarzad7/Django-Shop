from django.urls import path, include
from . import views


app_name = 'home'

bucket_urls = [
    path('', views.BucketHoneView.as_view(), name='bucket'),
    path('delete_obj/<str:key>/', views.DeleteBucketView.as_view(), name='delete_obj'),
    path('download_obj/<str:key>/', views.DownloadBucketView.as_view(), name='download_obj'),

]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]
