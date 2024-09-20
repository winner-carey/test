from django.db import models


# Create your models here.
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.EmailField()


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField()

    publish = models.ForeignKey(to='Publish', to_field='nid')
    authors = models.ManyToManyField(to='Author')


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

# class Book2Author(models.Model):
#     nid = models.AutoField(primary_key=True)
#     book = models.ForeignKey(to='Book', to_field='nid')
#     author = models.ForeignKey(to='Author', to_field='nid')
