from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    #video = models.FileField(upload_to='project_videos/')  [add this later when you are done making this]
    github_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='project_images/')
    
    def __str__(self):
        return f"Image for {self.project.title}"

class Contact(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"{self.name}, {self.email}: {self.message} at {self.created_at}"