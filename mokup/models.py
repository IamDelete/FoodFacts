from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import Group, Permission


class MyUser(AbstractUser):
    # Your custom fields here

    class Meta:
        # Use a unique table name for your custom user model
        db_table = 'my_custom_user_table'

    # Specify unique related_name for groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='myuser_custom_groups'
    )

    # Specify unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='myuser_custom_permissions'
    )


class food(models.Model):
    name = models.CharField(max_length = 150)
    desc = models.CharField(max_length= 500)
    kcal= models.IntegerField()
    pro = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()
