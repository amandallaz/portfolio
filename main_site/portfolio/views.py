from django.shortcuts import render
from .models import Project

def homepage(request):
    category = request.GET.get('category')  # e.g., ?category=apps
    if category:
        projects = Project.objects.filter(category__iexact=category)
    else:
        projects = Project.objects.all()
    return render(request, 'portfolio/homepage.html', {
        'projects': projects,
        'active_category': category,
    })


def about(request):
    return render(request, "portfolio/about.html")