from django.db import models


# Create your models here.
class Prevents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'tb_prevents'

# Prevents.objects.filter(id__in=[i for i in range(40, 100)]).delete()