from django.shortcuts import render
from .models import Feature

def about(request):
    features = Feature.objects.prefetch_related('person', 'company').all()
    return render(request, 'about_page.html', {'features': features})
