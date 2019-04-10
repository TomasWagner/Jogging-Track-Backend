from django.db import models 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an positive number'),
            params={'value': value},
        )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('U', 'User'),#(Key,Value)
        ('A', 'Admin'), 
        ('M', 'Manager')
    )
    role = models.CharField(max_length=10, choices=ROLES, default='U')

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    distance = models.IntegerField(validators=[validate_positive])
    time = models.IntegerField(validators=[validate_positive])