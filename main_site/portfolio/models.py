from django.db import models

# define project category options
CATEGORY_CHOICES = [
    ("apps", "Apps"),
    ("projects", "Projects"),
    ("photos", "Photos"),
]


# each object ("card") is a project
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    url = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="apps")

    def __str__(self):
        return self.title


# individual gallery photos, each project can have multiple photos (one:many)
class Photo(models.Model):
    project = models.ForeignKey(
        Project, related_name="photos", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="gallery_photos/")
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} - Photo {self.order}"
