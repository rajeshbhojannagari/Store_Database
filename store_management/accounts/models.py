from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    Role_choice=(
        ('seller','seller'),
        ('customer','customer')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=50,choices=Role_choice)
    phone=models.CharField(max_length=18,blank=True)
    address=models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.role}"
# Create your models here.
