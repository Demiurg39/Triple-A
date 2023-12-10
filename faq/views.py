from django.shortcuts import render
from .models import FAQ

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_page.html', {'faqs': faqs})
