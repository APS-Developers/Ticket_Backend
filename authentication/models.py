from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserPermission(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    CRM_permission = models.BooleanField(choices=BOOL_CHOICES)
    Inventory_permission = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return self.user.username
