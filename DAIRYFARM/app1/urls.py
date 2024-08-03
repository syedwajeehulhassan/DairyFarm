from django.urls import path,include

from app1 import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('contactapi', views.ContactViewset, basename='contactapi')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('gallery/', views.gallery, name='gallery'),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]