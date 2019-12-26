from django.db import models
from accounts.models import MyUser

# Create your models here.
class job_listing(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
        
    # Department choices and model field
    DEPARTMENT = [
        ('Sales','Sales'),
        ('HR ','HR'),
        ('Technology','Technology'),
        ('Accounts','Accounts'),
    ]
    department = models.CharField(
        max_length=15,
        choices=DEPARTMENT,
        default='Sales',
        blank=False
    )
        
    position = models.CharField(max_length=30)
    
    SALARY_CHOICES = [
        (2000,'2000'),
        (3000,'3000'),
        (4000,'4000'),
        (5000,'5000'),
        (6000,'6000'),
        (7000,'7000'),
        (8000,'8000'),
        (9000,'9000'),
        (10000,'10000'),

    ]
    salary = models.IntegerField(
        choices = SALARY_CHOICES,
        default = '4000'
    )
    def __str__(self):
        return (self.position)


