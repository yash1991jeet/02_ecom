from django.db import models

# Create your models here.
# We are making a database here.


class Product(models.Model):  # we are making a table named Product and inherit from models.Model.
    product_id = models.AutoField # it is integer field which automatically increments
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)  # description
    pub_date = models.DateField()  # these things (datafield, atofield, etc) can be read from django documentation.
