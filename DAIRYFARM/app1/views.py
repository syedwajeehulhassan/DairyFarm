from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app1/index.html')

def error (request):
    return render(request, 'app1/404.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')

def feature(request):
    return render(request, 'app1/feature.html')

def gallery(request):
    return render(request, 'app1/gallery.html')

def product(request):
    return render(request, 'app1/product.html')

def service(request):
    return render(request, 'app1/service.html')

def team(request):
    return render(request, 'app1/team.html')

def testimonial(request):
    return render(request, 'app1/testimonial.html')


from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer