from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User

# Create your models here.
class semOne(models.Model):
    SEM1_SUB1 = 'M1'
    SEM1_SUB2 = 'CHEMISTRY'
    SEM1_SUB3 = 'PHYSICS'
    SEM1_SUB4 = 'PYTHON'
    SEM1_SUB5 = 'ENGLISH'
    
    SEM1_YEAR = [
        (SEM1_SUB1, 'M1'),
        (SEM1_SUB2, 'CHEMISTRY'),
        (SEM1_SUB3, 'PHYSICS'),
        (SEM1_SUB4, 'PYTHON'),
        (SEM1_SUB5, 'ENGLISH')
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=SEM1_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(null=True)
    def __str__(self):
        return self.select_sub

class semTwo(models.Model):
    SEM2_SUB1 = 'M2'
    SEM2_SUB2 = 'PHYSICS'
    SEM2_SUB3 = 'BEEE'
    SEM2_SUB4 = 'C'
    SEM2_SUB5 = 'ENGINEERING GRAPHICS'
    SEM2_SUB6 = 'ENGLISH2'
    SEM2_YEAR = [
        (SEM2_SUB1, 'M2'),
        (SEM2_SUB2, 'PHYSICS'),
        (SEM2_SUB3, 'BEEE'),
        (SEM2_SUB4, 'C'),
        (SEM2_SUB5, 'ENGINEERING GRAPHICS'),
        (SEM2_SUB6, 'ENGLISH2'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=SEM2_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(null=True)
    def __str__(self):
        return self.select_sub

class semThree(models.Model):
    SEM3_SUB1 = 'M3'
    SEM3_SUB2 = 'DSA'
    SEM3_SUB3 = 'OOPS'
    SEM3_SUB4 = 'FDS'
    SEM3_SUB5 = 'DPCO'
    SEM3_YEAR = [
        (SEM3_SUB1, 'M3'),
        (SEM3_SUB2, 'DSA'),
        (SEM3_SUB3, 'OOPS'),
        (SEM3_SUB4, 'FDS'),
        (SEM3_SUB5, 'DPCO')
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=SEM3_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(null=True)
    def __str__(self):
        return self.select_sub

class semFour(models.Model):
    SEM4_SUB1 = 'ESS'
    SEM4_SUB2 = 'ALGORITHMS'
    SEM4_SUB3 = 'DBMS'
    SEM4_SUB4 = 'OS'
    SEM4_SUB5 = 'OOPS'
    SEM4_SUB6 = 'AIML'
    SEM4_YEAR = [
        (SEM4_SUB1, 'ESS'),
        (SEM4_SUB2, 'ALGORITHMS'),
        (SEM4_SUB3, 'DBMS'),
        (SEM4_SUB4, 'OS'),
        (SEM4_SUB5, 'OOPS'),
        (SEM4_SUB6, 'AIML'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=SEM4_YEAR,
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(null=True)

    def __str__(self):
        return self.select_sub

class notificationsLive(models.Model):
    title = CharField(max_length=250)
    dt = DateField(auto_now_add=True)

    def __str__(self):
        return self.title



