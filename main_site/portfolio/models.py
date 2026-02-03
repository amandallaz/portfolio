from django.db import models

CATEGORY_CHOICES = [
    ('apps', 'Apps'),
    ('projects', 'Projects'),
    ('photos', 'Photos'),

]
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='apps')  

    def __str__(self):
        return self.title