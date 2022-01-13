from django.contrib.admin.decorators import register
from django.db import models
from django.db.models.fields import proxy

# Create your models here.
class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Student (models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)
    def __str__(self):
        return self.firstname




##--------------------------model inheritance------------------
class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # abstract class not registered in admin
        # if its not abstract, it will be register
        ordering = ['title']

class ItemA(BaseItem):
    content = models.TextField()

    class Meta(BaseItem.Meta):
        ordering = ['-created']
    
class ItemB(BaseItem):
    file = models.FileField(upload_to='files')

class ItemC(BaseItem):
    file = models.FileField(upload_to='files')


class ItemD(BaseItem):
    file = models.SlugField( max_length=200, unique=True)




