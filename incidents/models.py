from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):

    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('councillor', 'Councillor'),
        ('municipality', 'Municipality'),
        ('mayor', 'Mayor'),
        ('admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='resident')
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Incident(models.Model):

    ISSUE_TYPES = [
        ('pothole', 'Pothole'),
        ('water', 'Water Leak'),
        ('power', 'Power Outage'),
        ('streetlight', 'Streetlight'),
        ('dumping', 'Illegal Dumping'),
        ('other', 'Other')
    ]

    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('reviewing', 'Under Review'),
        ('progress', 'In Progress'),
        ('resolved', 'Resolved')
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    issue_type = models.CharField(max_length=20,choices=ISSUE_TYPES)

    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=255)

    latitude = models.FloatField(blank=True, null=True)

    longitude = models.FloatField(blank=True, null=True)

    image = models.ImageField(upload_to='incidents/',blank=True,null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name="comments")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"