from django.shortcuts import render, get_object_or_404
from .models import Project


## HOMEPAGE
def homepage(request):

    # get category, filter projects if category selected
    category = request.GET.get("category")
    if category:
        projects = Project.objects.filter(category__iexact=category)
    else:
        projects = Project.objects.all()

    # render homepage template with project and category data
    return render(
        request,
        "portfolio/homepage.html",
        {
            "projects": projects,
            "active_category": category,
        },
    )


## GALLERY
def gallery(request, slug):
    # find project based on URL slug
    project = get_object_or_404(
        Project,
        title__iexact=slug.replace("-", " "),
        category="photos",
    )

    # get related photos
    photos_qs = project.photos.all()

    # build list of images for gallery, cover image first
    slides = []

    if project.image:
        slides.append(
            {
                "url": project.image.url,
                "caption": "",
                "is_cover": True,
            }
        )

    for photo in photos_qs:
        slides.append(
            {
                "url": photo.image.url,
                "caption": photo.caption,
                "is_cover": False,
            }
        )

    # render gallery template with project and slides data
    return render(
        request,
        "portfolio/gallery.html",
        {
            "project": project,
            "slides": slides,
        },
    )


## ABOUT
def about(request):
    # render static about page
    return render(request, "portfolio/about.html")
