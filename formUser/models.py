from django.db import models

class User(models.Model):

    usr_name = models.CharField(max_length=50)
    usr_email = models.EmailField(unique=True)
    usr_address = models.CharField(max_length=250)
    usr_City = models.CharField(max_length=250)

    class Meta:
        db_table='formUser'
