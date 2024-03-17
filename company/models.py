from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='company_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_key = models.CharField(max_length=15,null=True, blank=True)
    access_key_expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name