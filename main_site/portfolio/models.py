from django.db import models

CATEGORY_CHOICES = [
    ('apps', 'Apps'),
    ('data science', 'Data Science'),
    ('visualization', 'Visualization'),
]
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='visualization')  # <-- NEW

    def __str__(self):
        return self.title