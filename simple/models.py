from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to='images')
    csv_file = models.FileField(upload_to='csv') 
