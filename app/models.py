from django.db import models


# Create your models here.
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "tokens"


class Utils(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # You can set max_length as needed
    ai_apikey = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "utils"
